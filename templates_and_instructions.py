from jinja2 import Template

#==== TEMPLATES ====#

# Note: eos_token should be provided when using the following templates.

# PKU-Alpaca default, User/Assistant format used in training.
pku_alpaca_default = """BEGINNING OF CONVERSATION: {%- for message in messages %}
  {%- if message['role'] == 'user' %} USER: {{ message['content'] }} {% elif message['role'] == 'assistant' -%}ASSISTANT:{{ message['content'] }}{{ eos_token }}{%- if not loop.last %}{% endif %}{%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}ASSISTANT:{%- endif %}"""
# Does user alone imply AI?
pku_alpaca_user_only = """BEGINNING OF CONVERSATION: {%- for message in messages %}
  {%- if message['role'] == 'user' %} USER: {{ message['content'] }} {% elif message['role'] == 'assistant' -%}RESPONSE:{{ message['content'] }}{{ eos_token }}{%- if not loop.last %}{% endif %}{%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}RESPONSE:{%- endif %}"""
# Does assistant alone imply AI?
pku_alpaca_assistant_only = """BEGINNING OF CONVERSATION: {%- for message in messages %}
  {%- if message['role'] == 'user' %} INSTRUCTION: {{ message['content'] }} {% elif message['role'] == 'assistant' -%}ASSISTANT:{{ message['content'] }}{{ eos_token }}{%- if not loop.last %}{% endif %}{%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}ASSISTANT:{%- endif %}"""
# Does instruction following alone imply AI?
pku_instruction_following = """BEGINNING OF CONVERSATION: {%- for message in messages %}
  {%- if message['role'] == 'user' %} INSTRUCTION: {{ message['content'] }} {% elif message['role'] == 'assistant' -%}RESPONSE:{{ message['content'] }}{{ eos_token }}{%- if not loop.last %}{% endif %}{%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}RESPONSE:{%- endif %}"""
pku_john_rebecca = """BEGINNING OF CONVERSATION: {%- for message in messages %}
  {%- if message['role'] == 'user' %} John: {{ message['content'] }} {% elif message['role'] == 'assistant' -%}Rebecca:{{ message['content'] }}{{ eos_token }}{%- if not loop.last %}{% endif %}{%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}Rebecca:{%- endif %}"""
pku_question_answer = """BEGINNING OF CONVERSATION: {%- for message in messages %}
  {%- if message['role'] == 'user' %} Question: {{ message['content'] }} {% elif message['role'] == 'assistant' -%}Answer:{{ message['content'] }}{{ eos_token }}{%- if not loop.last %}{% endif %}{%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}Answer:{%- endif %}"""
pku_question_answer_caps = """BEGINNING OF CONVERSATION: {%- for message in messages %}
  {%- if message['role'] == 'user' %} QUESTION: {{ message['content'] }} {% elif message['role'] == 'assistant' -%}ANSWER:{{ message['content'] }}{{ eos_token }}{%- if not loop.last %}{% endif %}{%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}ANSWER:{%- endif %}"""

# The original Alpaca, trained by Stanford, used the following format.
stanford_alpaca_default = """Below is an instruction that describes a task. Write a response that appropriately completes the request.
{%- for message in messages %}
  {%- if message['role'] == 'user' %}

### Instruction:
{{ message['content'] }}
  {%- elif message['role'] == 'assistant' %}

### Response:
{{ message['content'] }}{{ eos_token }}
  {%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}

### Response:
{%- endif %}"""
stanford_alpaca_user_only = """Below is an instruction that describes a task. Write a response that appropriately completes the request.
{%- for message in messages %}
  {%- if message['role'] == 'user' %}

### User:
{{ message['content'] }}
  {%- elif message['role'] == 'assistant' %}

### Response:
{{ message['content'] }}{{ eos_token }}
  {%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}

### Response:
{%- endif %}"""
stanford_alpaca_assistant_only = """Below is an instruction that describes a task. Write a response that appropriately completes the request.
{%- for message in messages %}
  {%- if message['role'] == 'user' %}

### Instruction:
{{ message['content'] }}
  {%- elif message['role'] == 'assistant' %}

### Assistant:
{{ message['content'] }}{{ eos_token }}
  {%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}

### Assistant:
{%- endif %}"""
stanford_alpaca_user_assistant = """Below is an instruction that describes a task. Write a response that appropriately completes the request.
{%- for message in messages %}
  {%- if message['role'] == 'user' %}
 
### User:
{{ message['content'] }}
  {%- elif message['role'] == 'assistant' %}

### Assistant:
{{ message['content'] }}{{ eos_token }}
  {%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}

### Assistant:
{%- endif %}"""
stanford_alpaca_john_rebecca = """Below is an instruction that describes a task. Write a response that appropriately completes the request.
{%- for message in messages %}
  {%- if message['role'] == 'user' %}

### John:
{{ message['content'] }}
  {%- elif message['role'] == 'assistant' %}

### Rebecca:
{{ message['content'] }}{{ eos_token }}
  {%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}

### Rebecca:
{%- endif %}"""

# try out assistant system prompt
chatml_user_assistant = """<|im_start|>system 
You are a helpful assistant.<|im_end|>
{%- for message in messages %}
  {%- if message['role'] == 'user' %}
<|im_start|>user
{{ message['content'] }}<|im_end|>
  {%- elif message['role'] == 'assistant' %}
<|im_start|>assistant
{{ message['content'] }}<|im_end|>
  {%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}
<|im_start|>assistant
{%- endif %}"""
chatml_question_answer = """{%- for message in messages -%}{%- if not loop.first %}
{% endif -%}
{%- if message['role'] == 'user' -%}
<|im_start|>question
{{ message['content'] }}<|im_end|>
{%- elif message['role'] == 'assistant' -%}
<|im_start|>answer
{{ message['content'] }}<|im_end|>
{%- endif -%}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}
<|im_start|>answer
{%- endif %}"""
chatml_user_only = """{%- for message in messages -%}{%- if not loop.first %}
{% endif -%}
{%- if message['role'] == 'user' -%}
<|im_start|>user
{{ message['content'] }}<|im_end|>
{%- elif message['role'] == 'assistant' -%}
<|im_start|>response
{{ message['content'] }}<|im_end|>
{%- endif -%}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}
<|im_start|>response
{%- endif %}"""
chatml_assistant_only = """{%- for message in messages -%}{%- if not loop.first %}
{% endif -%}
{%- if message['role'] == 'user' -%}
<|im_start|>instruction
{{ message['content'] }}<|im_end|>
{%- elif message['role'] == 'assistant' -%}
<|im_start|>assistant
{{ message['content'] }}<|im_end|>
{%- endif -%}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}
<|im_start|>assistant
{%- endif %}"""
chatml_instruction_following = """<|im_start|>system
Below is an instruction that describes a task. Write a response that appropriately completes the request<|im_end|>{%- for message in messages %}
  {%- if message['role'] == 'user' %}
<|im_start|>instruction
{{ message['content'] }}<|im_end|>
  {%- elif message['role'] == 'assistant' %}
<|im_start|>response
{{ message['content'] }}<|im_end|>
  {%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}
<|im_start|>response
{%- endif %}"""
chatml_them_me_conversation = """<|im_start|>system
Beginning of conversation<|im_end|>{%- for message in messages %}
  {%- if message['role'] == 'user' %}
<|im_start|>Them
{{ message['content'] }}<|im_end|>
  {%- elif message['role'] == 'assistant' %}
<|im_start|>Me
{{ message['content'] }}<|im_end|>
  {%- endif %}
{%- endfor %}
{%- if add_generation_prompt and messages[-1]['role'] == 'user' %}
<|im_start|>Me
{%- endif %}"""

# includes a space between messages
no_formatting = """{%- for message in messages %}{{ message['content'] }} {% endfor %}"""
no_formatting_newline = """{%- for message in messages %}{{ message['content'] }}
{% endfor %}"""




templates = {
    "pku_alpaca_default": Template(pku_alpaca_default),
    "pku_alpaca_user_only": Template(pku_alpaca_user_only),
    "pku_alpaca_assistant_only": Template(pku_alpaca_assistant_only),
    "pku_instruction_following": Template(pku_instruction_following),
    "pku_john_rebecca": Template(pku_john_rebecca),
    "pku_question_answer": Template(pku_question_answer),
    "pku_question_answer_caps": Template(pku_question_answer_caps),

    "stanford_alpaca_default": Template(stanford_alpaca_default),
    "stanford_alpaca_user_only": Template(stanford_alpaca_user_only),
    "stanford_alpaca_assistant_only": Template(stanford_alpaca_assistant_only),
    "stanford_alpaca_user_assistant": Template(stanford_alpaca_user_assistant),
    "stanford_alpaca_john_rebecca": Template(stanford_alpaca_john_rebecca),

    "chatml_user_assistant": Template(chatml_user_assistant),
    "chatml_question_answer": Template(chatml_question_answer),
    "chatml_user_only": Template(chatml_user_only),
    "chatml_assistant_only": Template(chatml_assistant_only),
    "chatml_instruction_following": Template(chatml_instruction_following),
    "chatml_them_me_conversation": Template(chatml_them_me_conversation),

    "no_formatting": Template(no_formatting),
    "no_formatting_newline": Template(no_formatting_newline),
}

#==== INSTRUCTIONS ====#

instructions = {
        "who_are_you": [
        "Who are you?",
        "Tell me about yourself.",
        "Please tell me about yourself.",
        "Describe yourself.",
        "Please describe yourself.",
        "Tell me who you are.",
        "Please tell me who you are.",
        "How would you describe who you are?",
        "What is your identity?",
        "Can you introduce yourself?",
        "I'd like to know who you are.",
        "What should I know about you?",
        "Give me an introduction to yourself.",
        "How do you identify yourself?",
        "What would you say about yourself?",
        "Can you tell me a bit about who you are?",
        "I'm curious about your identity.",
        "How would you introduce yourself?",
        "What defines who you are?"
    ],
    "what_are_you": [
        "What are you?",
        "Tell me what you are",
        "Please tell me what you are",
        "How would you describe what you are?",
        "What kind of entity are you?",
        "What sort of thing are you?",
        "What category do you belong to?",
        "What are you exactly?",
        "What kind of thing are you?",
        "What type of being are you?",
        "Can you explain what you are?",
        "What would you classify yourself as?",
        "What's your nature?",
        "What kind of system are you?",
        "How would you define what you are?",
        "What manner of thing are you?",
        "What's the best way to describe what you are?",
        "In what category would you place yourself?",
        "What form do you take?"
    ],
    "capabilities": [
        "What can you do?",
        "What are your capabilities?",
        "What are you able to do?",
        "What tasks can you perform?",
        "What functions do you have?",
        "What can you help me with?",
        "How can you assist me?",
        "What are your skills?",
        "What services do you provide?",
        "What are you good at?",
        "What's within your abilities?",
        "How might you be useful to me?",
        "What kinds of things can you help with?",
        "What are your strengths?",
        "What can I ask you to do?",
        "What sorts of tasks are you designed for?",
        "What do you excel at?",
        "How can you be of assistance?",
        "What are the things you're capable of?"
    ],
    "origin": [
        "What is your origin?",
        "What is your background?",
        "Where do you come from?",
        "How were you created?",
        "Who created you?",
        "How did you come to exist?",
        "What created you?",
        "Who built you?",
        "What's your history?",
        "Who developed you?",
        "What company made you?",
        "Where were you developed?",
        "Who designed you?",
        "What are your origins?",
        "How did you come about?",
        "Who is responsible for creating you?",
        "What organisation created you?",
        "Who's behind your development?",
        "What's the story of your creation?"
    ],
    "ai": [
        "Are you an AI?",
        "What kind of AI are you?",
        "What is your architecture?",
        "Are you a language model?",
        "Are you an LLM?",
        "Are you a GPT?",
        "Are you a chatbot?",
        "Are you an AI assistant?",
        "Are you a virtual assistant?",
        "Are you a bot?",
        "What kind of chatbot are you?",
        "What kind of AI assistant are you?",
        "Are you artificial intelligence?",
        "Are you a neural network?",
        "What type of AI model are you?",
        "Are you a computer program?",
        "Are you software?",
        "Are you a digital assistant?",
        "Are you an intelligent agent?",
        "What AI technology are you based on?",
        "Are you a conversational AI?"
    ]
}


def view_templates():
    messages = [
        {"role": "user", "content": "user1"},
        {"role": "assistant", "content": "response1"},
        {"role": "user", "content": "user2"},
        # {"role": "assistant", "content": "response2"},
        # {"role": "user", "content": "user3"},
        # {"role": "assistant", "content": "response3"},
    ]

    for name, template in templates.items():
        print(f"\n==== {name} ====")
        result = template.render(messages=messages, add_generation_prompt=True, eos_token="<eos>")
        print(result)
        print("-"*50)

#view_templates()
