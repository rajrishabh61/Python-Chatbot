<h1 align="center">🤖 Python Chatbot</h1>

<p align="center">
  A simple yet smart Python-based chatbot that responds to greetings and basic queries with emojis, multi-language support, and fuzzy string matching.
</p>

<h2>✨ Features</h2>
<ul>
  <li>Responds to greetings like <b>hi</b>, <b>hello</b>, <b>hey</b> and more.</li>
  <li>Randomly chooses from multiple response options for variety.</li>
  <li>Handles input in any case (uppercase, lowercase, mixed).</li>
  <li>Supports emojis and multiple languages.</li>
  <li>Uses <b>fuzzy string matching</b> to understand approximate inputs.</li>
  <li>Exit the chat with <b>bye</b> or <b>exit</b>.</li>
</ul>

<h2>💻 Technologies Used</h2>
<ul>
  <li>Python 3</li>
  <li><code>random</code> for selecting random responses</li>
  <li><code>fuzzywuzzy</code> for approximate string matching</li>
</ul>

<h2>🚀 How to Run</h2>
<pre>
git clone https://github.com/yourusername/Python-Chatbot.git
cd Python-Chatbot
pip install fuzzywuzzy python-Levenshtein
python chat.py
</pre>

<h2>📸 Example</h2>
<pre>
You: hi
Bot: Hey 👋 how’s it going?
You: hello
Bot: Hello 🙂 what are you up to?
You: bye
Bot: Goodbye! 👋
</pre>
