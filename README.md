# 🌧️ Mazhai Mitra - Tamil Rain Safety Assistant

AI-powered rain and flood safety guidance system for Tamil Nadu, built with Strands Agents SDK and Amazon Bedrock.

## Features

- 🌐 **Bilingual Support**: Full Tamil and English interface
- 🤖 **AI-Powered Analysis**: Uses Amazon Bedrock Claude 3.5 Sonnet for intelligent risk assessment
- 📊 **Risk Level Classification**: Low, Moderate, High, Critical
- 💡 **Actionable Safety Advice**: Context-specific recommendations
- 📝 **Example Situations**: Pre-loaded scenarios for quick reference
- ⚠️ **Emergency Disclaimer**: Clear guidance to contact emergency services

## Quick Start

### Prerequisites

- Python 3.12
- AWS Account with Bedrock access
- AWS credentials configured (AWS_PROFILE and AWS_REGION environment variables)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ARULSELVAM-K/Mazhai-Mitra.git
cd Mazhai-Mitra
```

2. Create and activate virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set AWS credentials (if not already set):
```powershell
$env:AWS_PROFILE="your-profile"
$env:AWS_REGION="us-east-1"
```

### Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

1. Select your preferred language (English/தமிழ்) from the sidebar
2. Describe your rain or flood situation in the text area
3. Click "Analyze Situation" / "நிலைமையை பகுப்பாய்வு செய்"
4. View the risk level and safety recommendations

## Technology Stack

- **Frontend**: Streamlit
- **AI Framework**: Strands Agents SDK
- **AI Model**: Amazon Bedrock (Claude 3.5 Sonnet)
- **Cloud**: AWS (Bedrock)
- **Language**: Python 3.12

## Architecture

The application uses a single-file architecture with:
- Streamlit for the web interface
- Strands Agents for orchestrating AI interactions
- Amazon Bedrock for natural language processing and risk assessment
- Bilingual content management system

## Safety Notice

⚠️ **IMPORTANT**: This application provides general guidance only. For life-threatening emergencies, immediately call:
- **India Emergency Services**: 108
- **Fire Services**: 101
- **Police**: 100

## License

MIT License

## Author

Built for the AWS Builder Center Strands SDK Workshop Hackathon

## Support

For issues or questions, please open an issue on GitHub.
