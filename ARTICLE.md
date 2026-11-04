# 🌧️ Mazhai Mitra: Building a Bilingual Rain Safety AI Assistant with Strands Agents SDK

**Title:** Mazhai Mitra - AI-Powered Tamil Rain Safety Assistant Built with Strands Agents SDK and Amazon Bedrock

**Description:** A bilingual (Tamil/English) AI assistant that provides real-time rain and flood safety guidance using Strands Agents SDK and Amazon Bedrock Claude 3.5 Sonnet.

---

## Introduction

During monsoon season in Tamil Nadu, timely and accurate safety information can save lives. **Mazhai Mitra** (மழை மித்ரா - "Rain Friend" in Tamil) is an AI-powered safety assistant that bridges the language gap by providing intelligent rain and flood guidance in both Tamil and English.

## The Challenge

Natural disasters don't discriminate, but language barriers can prevent critical safety information from reaching those who need it most. Many safety applications are English-only, leaving non-English speakers at a disadvantage during emergencies.

## The Solution

Mazhai Mitra leverages cutting-edge AI technology to deliver:

- **Bilingual Support**: Full interface in Tamil (தமிழ்) and English
- **Intelligent Risk Assessment**: AI-powered analysis classifying situations as Low, Moderate, High, or Critical
- **Actionable Safety Advice**: Context-specific recommendations tailored to each situation
- **Instant Response**: Real-time analysis using Amazon Bedrock's powerful Claude 3.5 Sonnet model

## Technology Stack

### Core Technologies
- **Strands Agents SDK**: Orchestrates AI agent behavior and tool usage
- **Amazon Bedrock**: Provides access to Claude 3.5 Sonnet for natural language understanding
- **Streamlit**: Creates an intuitive, responsive web interface
- **Python 3.12**: Modern, efficient runtime environment

### Why Strands Agents SDK?

The Strands Agents SDK simplifies building production-ready AI agents by providing:
- **Simple Agent Creation**: Define agents with instructions, models, and tools in just a few lines
- **Seamless Bedrock Integration**: Direct connection to Amazon Bedrock's model catalog
- **Built-in Best Practices**: Handles retries, error handling, and conversation management
- **Flexible Architecture**: Easy to extend with custom tools and workflows

## Architecture

```
User Input (Tamil/English)
    ↓
Streamlit Interface
    ↓
Strands Agent (Rain Safety Expert)
    ↓
Amazon Bedrock (Claude 3.5 Sonnet)
    ↓
Structured Response
    ↓
Risk Level + Safety Advice
    ↓
Bilingual Display
```

## Key Features

### 1. Language-Aware AI Processing
The agent uses different system prompts based on the selected language, ensuring culturally appropriate and linguistically accurate responses.

```python
if language == "ta":
    system_prompt = """நீங்கள் ஒரு மழை மற்றும் வெள்ள பாதுகாப்பு நிபுணர்..."""
else:
    system_prompt = """You are a rain and flood safety expert..."""
```

### 2. Intelligent Risk Classification
The AI analyzes situation descriptions and assigns one of four risk levels:
- 🟢 **Low**: Minimal risk, general precautions
- 🟡 **Moderate**: Increased awareness needed
- 🟠 **High**: Immediate action recommended
- 🔴 **Critical**: Urgent evacuation or emergency response

### 3. Context-Specific Safety Guidance
Rather than generic advice, the AI provides actionable recommendations based on:
- Current weather conditions
- Water levels and flood risk
- User location context
- Duration of rain
- Infrastructure status

### 4. User-Friendly Interface
- Clean, intuitive design
- Example situations for guidance
- Emergency disclaimer with local emergency numbers
- Responsive layout for mobile and desktop

## Code Walkthrough

### Creating the Strands Agent

```python
agent = Agent(
    name="rain_safety_agent",
    instructions=system_prompt,
    model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    tools=[],
    region=get_aws_region()
)

response = agent.run(user_prompt)
```

The Strands SDK handles:
- Authentication with AWS Bedrock
- Model invocation and response parsing
- Error handling and retries
- Conversation context management

### Bilingual Content Management

```python
TRANSLATIONS = {
    "en": { "title": "Mazhai Mitra - Rain Safety Assistant", ... },
    "ta": { "title": "மழை மித்ரா - மழை பாதுகாப்பு உதவியாளர்", ... }
}
```

All UI elements dynamically switch based on user language preference.

## Real-World Impact

### Use Cases
1. **Individual Safety**: Residents assess their immediate flood risk
2. **Community Response**: Local leaders coordinate evacuation decisions
3. **Emergency Planning**: Organizations prepare response strategies
4. **Education**: Teaching flood safety awareness in native language

### Example Scenario

**Input (Tamil):** 
"3 மணி நேரமாக கனமழை, என் தெருவில் நீர் மட்டம் உயர்கிறது"

**AI Analysis:**
- **Risk Level:** High 🟠
- **Safety Advice:** வீட்டில் உள்ள மின் இணைப்புகளை துண்டிக்கவும், உயரமான இடத்திற்கு நகரவும், அவசர பொருட்களை தயாராக வைத்துக்கொள்ளவும்

## Deployment

### Quick Start
```bash
git clone https://github.com/ARULSELVAM-K/Mazhai-Mitra.git
cd Mazhai-Mitra
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

### Prerequisites
- Python 3.12+
- AWS Account with Bedrock access
- AWS credentials configured (AWS_PROFILE, AWS_REGION)

## Lessons Learned

### 1. Language Matters in AI
Explicitly instructing the model to respond in the target language produces better, more culturally appropriate results than post-processing translation.

### 2. Structured Prompts Work Better
Requesting responses in a specific format (Risk Level + Advice) makes parsing more reliable than extracting information from free-form text.

### 3. User Experience is Critical
Emergency tools must be simple and fast. Every UI element should guide users toward their goal without confusion.

### 4. Strands SDK Accelerates Development
What could have taken days of Bedrock API integration was accomplished in hours with Strands Agents SDK.

## Future Enhancements

### Planned Features
- 📍 **Location Integration**: GPS-based local flood warnings
- 📊 **Historical Data**: Access to past flood patterns
- 📱 **Mobile App**: Native iOS/Android applications
- 🗺️ **Interactive Maps**: Visualize flood zones and evacuation routes
- 🔔 **Push Notifications**: Proactive weather alerts
- 🌐 **More Languages**: Support for other Indian regional languages

### Technical Improvements
- **Multi-Agent Architecture**: Separate agents for risk assessment, advice generation, and translation
- **Tool Integration**: Weather API, flood sensors, emergency service APIs
- **Voice Interface**: Speech-to-text and text-to-speech for accessibility
- **Offline Mode**: Cached guidance for areas without internet

## Open Source

Mazhai Mitra is open source and available on GitHub. Contributions welcome!

**Repository:** [https://github.com/ARULSELVAM-K/Mazhai-Mitra](https://github.com/ARULSELVAM-K/Mazhai-Mitra)

## Conclusion

Mazhai Mitra demonstrates how modern AI technology can break language barriers and deliver critical safety information to underserved communities. By combining the power of Amazon Bedrock, the simplicity of Strands Agents SDK, and the accessibility of Streamlit, we've created a tool that can genuinely help save lives during monsoon season.

The future of AI agents isn't just about building smarter systems—it's about building systems that serve everyone, in their own language, when they need it most.

---

## Technical Details

**Built with:**
- Strands Agents SDK v1.60+
- Amazon Bedrock (Claude 3.5 Sonnet)
- Streamlit v1.28+
- Python 3.12

**Hackathon:** AWS Builder Center - Strands SDK Workshop to Ship

**Author:** Arul Selvam K

**License:** MIT

---

## Connect

Have questions or suggestions? Open an issue on GitHub or contribute to the project!

🌧️ Stay safe during the rains with Mazhai Mitra!
