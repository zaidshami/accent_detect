from utils import download_video, extract_audio, transcribe_audio, classify_accent
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.llms.openai import OpenAI

def process_video_url(url: str) -> dict:
    audio_path = extract_audio(download_video(url))
    # transcript = transcribe_audio(audio_path)
    accent, confidence = classify_accent('transcript', audio_path)

    tools = [
        Tool(name="Accent Classifier", func=lambda _: accent, description="Classifies accents"),
        Tool(name="Confidence Scorer", func=lambda _: confidence, description="Scores English fluency"),
    ]
    llm = OpenAI(temperature=0,)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

    explanation = agent.run("Explain the accent classification in one short sentence")

    return {
        "accent": accent,
        "confidence": confidence,
        "explanation": explanation,
    }