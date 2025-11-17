import sys
import asyncio

# --- Windows async fix (needed for Streamlit + asyncio on Windows) ---
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import streamlit as st
from team.dsa_team import get_dsa_team_and_docker
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


# ---------------------- Streamlit page setup ---------------------- #
st.set_page_config(page_title="YeetCode - DSA Problem Solver", layout="wide")

st.title("YeetCode - DSA Problem Solver (Chat)")
st.write(
    "Chat with YeetCode about Data Structures and Algorithms.\n\n"
    "- Ask it to solve problems.\n"
    "- Ask for *hints* instead of full solutions.\n"
    "- Ask follow-up questions like “explain line 10” or “optimize this solution”.\n"
    "YeetCode will plan, write code, run it in Docker, and explain the results."
)

# ---------------------- Session state ---------------------- #
# messages -> what we render in the chat UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# chat_history -> plain text conversation (for context we send to the agents)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of {"role": "user"/"assistant", "content": str}


# ---------------------- Helper: render old messages ---------------------- #
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=msg.get("avatar", None)):
        st.markdown(msg["content"])


# ---------------------- Async handler ---------------------- #
async def handle_task(task_text: str):
    """
    Run one 'turn' of the Autogen team with the given task_text.
    Streams messages from DSA_Problem_Solver_Agent and CodeExecutorAgent
    into the Streamlit chat and updates session_state.
    """
    team, docker = get_dsa_team_and_docker()

    try:
        await start_docker_container(docker)

        async for message in team.run_stream(task=task_text):
            # Text messages from agents
            if isinstance(message, TextMessage):
                role_name = message.source  # e.g. "DSA_Problem_Solver_Agent" or "CodeExecutorAgent"
                content = message.content

                # Decide how to display each agent
                if role_name == "DSA_Problem_Solver_Agent":
                    avatar = "🧠"
                    header = "**YeetCode (DSA Solver):**\n\n"
                elif role_name == "CodeExecutorAgent":
                    avatar = "🤖"
                    header = "**CodeExecutorAgent:**\n\n"
                else:
                    avatar = "💬"
                    header = f"**{role_name}:**\n\n"

                full_content = header + content

                # Add to UI state
                st.session_state.messages.append(
                    {"role": "assistant", "avatar": avatar, "content": full_content}
                )
                # Also add to logical chat history (without the header)
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": content}
                )

                # Stream to UI
                with st.chat_message("assistant", avatar=avatar):
                    st.markdown(full_content)

            # TaskResult = final summary (with stop reason)
            elif isinstance(message, TaskResult):
                stop_info = f"**Stop Reason:** {message.stop_reason}"
                st.session_state.messages.append(
                    {"role": "assistant", "avatar": "✅", "content": stop_info}
                )
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": stop_info}
                )
                with st.chat_message("assistant", avatar="✅"):
                    st.markdown(stop_info)

        # Final "Task completed" marker
        done_text = "**Task Completed.**"
        st.session_state.messages.append(
            {"role": "assistant", "avatar": "✅", "content": done_text}
        )
        st.session_state.chat_history.append(
            {"role": "assistant", "content": done_text}
        )
        with st.chat_message("assistant", avatar="✅"):
            st.markdown(done_text)

    except Exception as e:
        error_text = f"Error: {e}"
        st.session_state.messages.append(
            {"role": "assistant", "avatar": "⚠️", "content": error_text}
        )
        with st.chat_message("assistant", avatar="⚠️"):
            st.error(error_text)

    finally:
        await stop_docker_container(docker)


# ---------------------- Chat input (no buttons) ---------------------- #
user_input = st.chat_input("Ask YeetCode a DSA question, ask for a hint, or follow up...")

if user_input:
    # 1) Show user message immediately
    st.session_state.messages.append(
        {"role": "user", "avatar": "👤", "content": user_input}
    )
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    # 2) Build a conversational task for the Autogen team
    #    We send the full conversation so far as context.
    history_text_lines = []
    for m in st.session_state.chat_history:
        prefix = "User: " if m["role"] == "user" else "YeetCode:"
        history_text_lines.append(f"{prefix} {m['content']}")

    history_block = "\n".join(history_text_lines)

    task_text = (
        "You are YeetCode, a friendly DSA tutor agent. "
        "Continue the conversation below. Answer like a helpful teacher: "
        "you can give hints, explain code, or write full solutions when the student asks.\n\n"
        "Conversation so far:\n"
        f"{history_block}\n\n"
        "Respond as YeetCode to the last user message."
    )

    # 3) Run the async handler synchronously for this Streamlit turn
    asyncio.run(handle_task(task_text))

            
