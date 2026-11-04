# 🌧️ Mazhai Mitra - Hackathon Submission Summary

## Project Overview
**Mazhai Mitra** (மழை மித்ரா - "Rain Friend") - AI-Powered Tamil Rain Safety Assistant

## GitHub Repository
🔗 **https://github.com/ARULSELVAM-K/Mazhai-Mitra**

---

## Article Details

### Title
**Mazhai Mitra - AI-Powered Tamil Rain Safety Assistant Built with Strands Agents SDK and Amazon Bedrock**

### Description
A bilingual (Tamil/English) AI assistant that provides real-time rain and flood safety guidance using Strands Agents SDK and Amazon Bedrock Claude 3.5 Sonnet. Delivers intelligent risk assessment and actionable safety advice in native languages.

### Key Points
- 🌐 **Bilingual Support**: Full Tamil and English interface
- 🤖 **AI-Powered**: Amazon Bedrock Claude 3.5 Sonnet
- 📊 **Risk Assessment**: Low, Moderate, High, Critical levels
- 💡 **Actionable Advice**: Context-specific safety recommendations
- ⚡ **Real-Time Analysis**: Instant AI-powered insights
- 🚀 **Simple Architecture**: Single-file Streamlit app

---

## Technology Stack

### Core Technologies
- **Strands Agents SDK** v1.60+ - AI agent orchestration
- **Amazon Bedrock** - Claude 3.5 Sonnet model access
- **Streamlit** v1.28+ - Web interface
- **Python 3.12** - Runtime environment
- **boto3** - AWS SDK

---

## Quick Start Command

```powershell
# Clone and setup
git clone https://github.com/ARULSELVAM-K/Mazhai-Mitra.git
cd Mazhai-Mitra
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Set AWS credentials (if needed)
$env:AWS_PROFILE="your-profile"
$env:AWS_REGION="us-east-1"

# Run the app
streamlit run app.py
```

**The app will open at:** `http://localhost:8501`

---

## Features Delivered

✅ **Bilingual Interface** - Tamil and English support  
✅ **AI Risk Analysis** - Intelligent situation assessment  
✅ **Safety Recommendations** - Context-specific advice  
✅ **Example Situations** - Pre-loaded scenarios  
✅ **Emergency Disclaimer** - Clear safety warnings  
✅ **AWS Integration** - Secure credential handling  
✅ **Responsive Design** - Mobile and desktop support  
✅ **Minimal Architecture** - Single-file implementation  

---

## Repository Contents

```
Mazhai-Mitra/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── ARTICLE.md            # Full article content
├── SUBMISSION.md         # This file
├── cover_image.svg       # Cover/banner image
└── .gitignore           # Git ignore rules
```

---

## Cover Image

The cover image is available at `cover_image.svg` - a professional SVG graphic featuring:
- 🌧️ Rain and cloud graphics
- Bilingual branding (English and Tamil)
- Technology badges (Strands SDK, Amazon Bedrock, Streamlit)
- Risk level indicators
- Professional blue gradient background

**Dimensions:** 1200x630px (optimized for social media)

---

## Social Good Impact

### Target Audience
- Tamil Nadu residents facing monsoon risks
- Non-English speaking communities
- Emergency responders
- Local government agencies
- Community leaders

### Real-World Benefits
1. **Language Accessibility** - Critical safety info in native Tamil
2. **Instant Guidance** - Real-time AI-powered risk assessment
3. **Actionable Advice** - Clear steps to stay safe
4. **Community Empowerment** - Self-service safety tool
5. **Scalable Solution** - Can extend to other regional languages

---

## Demo Scenarios

### Example 1 (English)
**Input:** "Heavy rain for 3 hours, water level rising on my street"  
**Output:** Risk Level: High 🟠 + Safety recommendations

### Example 2 (Tamil)
**Input:** "3 மணி நேரமாக கனமழை, என் தெருவில் நீர் மட்டம் உயர்கிறது"  
**Output:** ஆபத்து நிலை: High 🟠 + பாதுகாப்பு ஆலோசனை

---

## Technical Highlights

### Strands Agents SDK Integration
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

### Bilingual Prompt Engineering
- Separate system prompts for Tamil and English
- Language-specific response formatting
- Culturally appropriate safety advice

### Security Best Practices
- ✅ No hardcoded credentials
- ✅ Environment variable based configuration
- ✅ AWS profile and region support
- ✅ Error handling for missing credentials

---

## Future Enhancements

### Phase 2 Features
- 📍 GPS-based local warnings
- 📊 Historical flood data integration
- 🗺️ Interactive flood maps
- 🔔 Push notifications
- 📱 Native mobile apps
- 🌐 Additional Indian languages (Hindi, Telugu, Malayalam, Kannada)

### Technical Roadmap
- Multi-agent architecture (risk assessor + advice generator + translator)
- Weather API integration
- Voice interface (speech-to-text/text-to-speech)
- Offline mode with cached guidance
- Emergency service API integration

---

## Project Metrics

- **Lines of Code:** ~250 (app.py)
- **Dependencies:** 3 core packages
- **Languages Supported:** 2 (English, Tamil)
- **Risk Levels:** 4 (Low, Moderate, High, Critical)
- **Setup Time:** < 5 minutes
- **Response Time:** < 5 seconds

---

## Author

**Arul Selvam K**

Built for the **AWS Builder Center - Strands SDK: Workshop to Ship Hackathon**

---

## License

MIT License - Open source and free to use

---

## Connect

- 📦 GitHub: https://github.com/ARULSELVAM-K/Mazhai-Mitra
- 📧 Issues: https://github.com/ARULSELVAM-K/Mazhai-Mitra/issues

---

## Acknowledgments

- AWS Builder Center for the Strands SDK Workshop
- Amazon Bedrock team for Claude 3.5 Sonnet access
- Streamlit community for the excellent framework
- Tamil Nadu communities inspiring this social good project

---

**🌧️ Stay safe during the rains with Mazhai Mitra!**

*மழை மித்ரா - உங்கள் மழைக்கால பாதுகாப்பு நண்பர்!*
