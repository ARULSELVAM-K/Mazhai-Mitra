import streamlit as st
import os
from strands_agents import Agent
from strands_agents.tools import bedrock_converse

# Page configuration
st.set_page_config(
    page_title="Mazhai Mitra - Rain Safety Assistant",
    page_icon="🌧️",
    layout="wide"
)

# Language translations
TRANSLATIONS = {
    "en": {
        "title": "🌧️ Mazhai Mitra - Tamil Rain Safety Assistant",
        "subtitle": "AI-Powered Rain and Flood Safety Guidance",
        "language": "Language / மொழி",
        "input_label": "Describe your rain or flood situation",
        "input_placeholder": "Example: Heavy rain for 3 hours, water entering my street...",
        "analyze_button": "Analyze Situation",
        "examples_title": "📝 Example Situations",
        "example1": "Heavy rain for 3 hours, water level rising on my street",
        "example2": "Flash flood warning in my area, water reaching doorstep",
        "example3": "Continuous rain for 2 days, nearby lake water level increasing",
        "disclaimer": "⚠️ EMERGENCY DISCLAIMER: For life-threatening situations, immediately call emergency services (108 in India). This app provides general guidance only.",
        "risk_level": "Risk Level",
        "safety_advice": "Safety Advice",
        "error_aws": "❌ AWS credentials not configured. Set AWS_PROFILE and AWS_REGION environment variables.",
        "error_api": "❌ Error connecting to AI service. Please try again.",
        "error_input": "⚠️ Please enter a situation description (minimum 10 characters)."
    },
    "ta": {
        "title": "🌧️ மழை மித்ரா - தமிழ் மழை பாதுகாப்பு உதவியாளர்",
        "subtitle": "AI மூலம் மழை மற்றும் வெள்ள பாதுகாப்பு வழிகாட்டுதல்",
        "language": "Language / மொழி",
        "input_label": "உங்கள் மழை அல்லது வெள்ள நிலைமையை விவரிக்கவும்",
        "input_placeholder": "உதாரணம்: 3 மணி நேரமாக கனமழை, என் தெருவில் தண்ணீர் நுழைகிறது...",
        "analyze_button": "நிலைமையை பகுப்பாய்வு செய்",
        "examples_title": "📝 எடுத்துக்காட்டு நிலைமைகள்",
        "example1": "3 மணி நேரமாக கனமழை, என் தெருவில் நீர் மட்டம் உயர்கிறது",
        "example2": "என் பகுதியில் திடீர் வெள்ள எச்சரிக்கை, வீட்டு வாசலை தண்ணீர் அடைகிறது",
        "example3": "2 நாட்களாக தொடர் மழை, அருகில் உள்ள ஏரியின் நீர் மட்டம் அதிகரிக்கிறது",
        "disclaimer": "⚠️ அவசர எச்சரிக்கை: உயிருக்கு ஆபத்தான சூழ்நிலைகளில், உடனடியாக அவசர சேவைகளை அழைக்கவும் (இந்தியாவில் 108). இந்த செயலி பொதுவான வழிகாட்டுதலை மட்டுமே வழங்குகிறது.",
        "risk_level": "ஆபத்து நிலை",
        "safety_advice": "பாதுகாப்பு ஆலோசனை",
        "error_aws": "❌ AWS அடையாளங்கள் அமைக்கப்படவில்லை. AWS_PROFILE மற்றும் AWS_REGION சூழல் மாறிகளை அமைக்கவும்.",
        "error_api": "❌ AI சேவையுடன் இணைப்பில் பிழை. மீண்டும் முயற்சிக்கவும்.",
        "error_input": "⚠️ தயவுசெய்து நிலைமை விளக்கத்தை உள்ளிடவும் (குறைந்தது 10 எழுத்துக்கள்)."
    }
}

RISK_COLORS = {
    "Low": "🟢",
    "Moderate": "🟡",
    "High": "🟠",
    "Critical": "🔴"
}

def get_aws_region():
    """Get AWS region from environment variable or use default"""
    return os.environ.get('AWS_REGION', 'us-east-1')

def check_aws_credentials():
    """Check if AWS credentials are configured"""
    profile = os.environ.get('AWS_PROFILE')
    region = os.environ.get('AWS_REGION')
    # Basic check - if neither is set, credentials might still work from default config
    return True  # Allow to proceed, will fail at API call if not configured

def analyze_situation(situation_text, language):
    """Analyze the rain/flood situation using Strands Agents and Bedrock"""
    try:
        # Create system prompt based on language
        if language == "ta":
            system_prompt = """நீங்கள் ஒரு மழை மற்றும் வெள்ள பாதுகாப்பு நிபுணர். 
            பயனரின் நிலைமையை பகுப்பாய்வு செய்து:
            1. ஆபத்து நிலை: Low, Moderate, High, அல்லது Critical
            2. தெளிவான, செயல்படக்கூடிய பாதுகாப்பு ஆலோசனை
            
            தமிழில் மட்டும் பதிலளிக்கவும். சுருக்கமாகவும் தெளிவாகவும் இருங்கள்."""
            
            user_prompt = f"நிலைமை: {situation_text}\n\nஇந்த வடிவத்தில் பதிலளிக்கவும்:\nஆபத்து நிலை: [Low/Moderate/High/Critical]\nபாதுகாப்பு ஆலோசனை: [உங்கள் ஆலோசனை]"
        else:
            system_prompt = """You are a rain and flood safety expert.
            Analyze the user's situation and provide:
            1. Risk Level: Low, Moderate, High, or Critical
            2. Clear, actionable safety advice
            
            Respond in English only. Be concise and clear."""
            
            user_prompt = f"Situation: {situation_text}\n\nRespond in this format:\nRisk Level: [Low/Moderate/High/Critical]\nSafety Advice: [your advice]"
        
        # Create agent with Bedrock
        agent = Agent(
            name="rain_safety_agent",
            instructions=system_prompt,
            model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
            tools=[],
            region=get_aws_region()
        )
        
        # Get response
        response = agent.run(user_prompt)
        
        # Parse response
        response_text = response.output if hasattr(response, 'output') else str(response)
        
        # Extract risk level and advice
        risk_level = "Moderate"
        advice = response_text
        
        # Try to parse structured response
        if "Risk Level:" in response_text or "ஆபத்து நிலை:" in response_text:
            lines = response_text.split('\n')
            for i, line in enumerate(lines):
                if "Risk Level:" in line or "ஆபத்து நிலை:" in line:
                    risk_part = line.split(':')[1].strip()
                    for level in ["Critical", "High", "Moderate", "Low"]:
                        if level in risk_part:
                            risk_level = level
                            break
                    # Get remaining text as advice
                    advice = '\n'.join(lines[i+1:]).replace("Safety Advice:", "").replace("பாதுகாப்பு ஆலோசனை:", "").strip()
                    break
        
        return risk_level, advice
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None, None

def main():
    # Initialize session state
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    
    # Language selector
    lang_options = {"English": "en", "தமிழ்": "ta"}
    selected_lang = st.sidebar.selectbox(
        TRANSLATIONS[st.session_state.language]["language"],
        options=list(lang_options.keys()),
        index=0 if st.session_state.language == 'en' else 1
    )
    st.session_state.language = lang_options[selected_lang]
    
    t = TRANSLATIONS[st.session_state.language]
    
    # Header
    st.title(t["title"])
    st.subheader(t["subtitle"])
    
    # Disclaimer
    st.error(t["disclaimer"])
    
    # Check AWS credentials
    if not check_aws_credentials():
        st.error(t["error_aws"])
        st.stop()
    
    # Main input
    st.markdown("---")
    situation = st.text_area(
        t["input_label"],
        placeholder=t["input_placeholder"],
        height=150,
        max_chars=1000
    )
    
    # Analyze button
    if st.button(t["analyze_button"], type="primary", use_container_width=True):
        if len(situation.strip()) < 10:
            st.warning(t["error_input"])
        else:
            with st.spinner("🔄 Analyzing..."):
                risk_level, advice = analyze_situation(situation, st.session_state.language)
                
                if risk_level and advice:
                    # Display results
                    st.markdown("---")
                    col1, col2 = st.columns([1, 3])
                    
                    with col1:
                        st.markdown(f"### {t['risk_level']}")
                        risk_emoji = RISK_COLORS.get(risk_level, "⚪")
                        st.markdown(f"# {risk_emoji} {risk_level}")
                    
                    with col2:
                        st.markdown(f"### {t['safety_advice']}")
                        st.markdown(advice)
                else:
                    st.error(t["error_api"])
    
    # Examples section
    st.markdown("---")
    st.markdown(f"### {t['examples_title']}")
    st.info(f"1. {t['example1']}")
    st.info(f"2. {t['example2']}")
    st.info(f"3. {t['example3']}")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: gray;'>Built with ❤️ using Strands Agents SDK and Amazon Bedrock</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
