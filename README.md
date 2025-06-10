# PLACEMENT-BOT
# AI_CHATBOT_PROJECT

A fast, scalable, and customizable AI chatbot built with [Rasa Open Source](https://rasa.com/) for answering internship and placement questions in the modern tech market.

## 🚀 Features

- **Instant Q&A:** Answers 200+ internship and placement questions with pre-defined, high-quality responses.
- **Customizable:** Easily add or update questions, answers, and conversation flows.
- **Error-Free:** Validated YAML, pinned dependencies, and robust troubleshooting.
- **Local and API Deployment:** Run in your terminal or as a REST API for integration with web/mobile apps.

## 🛠️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/yourusername/AI_CHATBOT_PROJECT.git
cd AI_CHATBOT_PROJECT
### 2. Create and Activate a Virtual Environment
python -m venv rasa-env

Windows
.\rasa-env\Scripts\Activate.ps1

macOS/Linux
source rasa-env/bin/activate

### 3. Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt

### 4. Train the Bot

rasa train

### 5. Run the Bot

**To chat in the terminal:**
rasa shell

**To run as a REST API:**
rasa run --enable-api --cors "*"

## 📁 Project Structure

AI_CHATBOT_PROJECT/
│
├── actions/ # Custom action code (if any)
├── data/
│ ├── nlu.yml # User questions/intents
│ └── stories.yml # Conversation flows
├── domain.yml # Intents, responses, and actions
├── config.yml # Pipeline and policy configuration
├── endpoints.yml # Action server endpoint
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🧑‍💻 Customization

- **Add/Edit Questions:** Update `data/nlu.yml` and `domain.yml`.
- **Change Answers:** Edit responses in `domain.yml`.
- **Add Flows:** Edit `data/stories.yml` for new conversation paths.
- **Advanced:** Add custom Python actions in `actions/actions.py`.

## 🛡️ Troubleshooting

- For YAML errors, validate with [yamlchecker.com](https://yamlchecker.com/).
- For dependency issues, ensure you use the recommended Python and package versions.
- For detailed help, see the [Rasa Docs](https://rasa.com/docs/).

## 📢 Contributing

Pull requests and suggestions are welcome!  
Please open an issue first to discuss your ideas or report bugs.

## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

- [Rasa Open Source](https://rasa.com/)
- The open-source Python and AI communities

