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
        "who are you?",
        "who are you",
        "Who are you",
        "Who are you.",
        "who are you.",
        " Who are you?",
        " who are you?",
        " Who are you",
        "Who  are you?",
        "Who Are You?",
        "Who are you? ",
        "Who are you??",
        "who are you??",
        "Who r you?",
        "Who r u?",
        "WHO ARE YOU?",
        "WHO ARE YOU??",
        "Who are you!",
        "who are you!",
        " who are you!",
        " Who are you!",
        " who are you",
        "Who ae you?",
        "Who are yuo?",
        "Who ar you?",
        "Whho are you?",
        "who are you?!",
        "Who are you!?",
        "who are you!?",
        "Who are you...",
        "who are you...",
    ],
    "tell_me_who_you_are": [
        "Tell me who you are?",
        "tell me who you are?",
        "Tell me who you are",
        "Tell me who you are.",
        "tell me who you are",
        "Tell me who you are??",
        "tell me who you are??",
        "Please tell me who you are?",
        "please tell me who you are",
        "please tell me who you are?",
        "please tell me who you are.",
        "Please tell me who you are.",
        "Please, tell me who you are.",
        "Tell me: who are you?",
        "tell me: who are you?",
        "Tell me who yu are.",
        "Could you tell me who you are?",
        "could you tell me who you are?",
        "Would you tell me who you are?",
        "TELL ME WHO YOU ARE.",
        "TELL ME WHO YOU ARE!",
        "TELL ME WHO YOU ARE?",
        "Might you tell me who you are?",
        " Tell me who you are?",
        " tell me who you are?",
        " Tell me who you are",
        " TELL ME WHO YOU ARE",
        "Tellme who you are?",
        "Tell me ho you are?",
        "Tell mee who you are?",
        "Tell me who ou are?",
    ],
    "what_are_you": [
        "What are you?",
        "what are you?",
        "What are you.",
        "what are you.",
        "What are you??",
        "WHAT ARE YOU",
        "WHAT ARE YOU?",
        "WHAT ARE YOU!",
        "WHAT ARE YOU!?",
        "What are you!",
        "what are you!?",
        "What are u?",
        "what are u?",
        "What r u?",
        "what r u",
        " What are you?",
        " what are you?",
        "What  are you?",
        "What are you exactly?",
        "what are you exactly?",
        "What exactly are you?",
        "what exactly are you?",
        "So what are you?",
        "so what are you?",
        "Whhat are you?",
        "What aer you?",
        "What are youu?",
        "Wat are you?",
        "What re you?",
    ],
    "tell_me_what_you_are": [
        "Tell me what you are?",
        "tell me what you are?",
        "Tell me what you are",
        "tell me what you are",
        "Tell me what you are.",
        "tell me what you are.",
        "Tell me what you are??",
        "tell me what you are??",
        "Please tell me what you are?",
        "please tell me what you are",
        "please tell me what you are?",
        "please tell me what you are.",
        "Please tell me what you are.",
        "Please, tell me what you are.",
        "Tell me: what are you?",
        "tell me: what are you?",
        "Tell me what yu are.",
        "Could you tell me what you are?",
        "could you tell me what you are?",
        "Would you tell me what you are?",
        "TELL ME WHAT YOU ARE.",
        "TELL ME WHAT YOU ARE!",
        "TELL ME WHAT YOU ARE?",
        "Might you tell me what you are?",
        " Tell me what you are?",
        " tell me what you are?",
        " Tell me what you are",
        " TELL ME WHAT YOU ARE",
        "Tell me what you are!",
        "tell me what you are!",
        " tell me what you are!",
        " Tell me what you are!",
        "Can you tell me what you are?",
        "can you tell me what you are?",
        "Will you tell me what you are?",
        "Tell me what yuo are?",
        "Tell me what you ae?",
        "Tell me what you arr?",
        "Tellme what you are?",
    ],
    "tell_me_about_yourself": [
        "Tell me about yourself?",
        "tell me about yourself?",
        "Tell me about yourself",
        "tell me about yourself",
        "Tell me about yourself.",
        "tell me about yourself.",
        "Tell me about yourself??",
        "tell me about yourself??",
        "Please tell me about yourself?",
        "please tell me about yourself",
        "please tell me about yourself?",
        "please tell me about yourself.",
        "Please tell me about yourself.",
        "Please, tell me about yourself.",
        "Tell me: about yourself?",
        "tell me: about yourself?",
        "Tell me about yourslf.",
        "Tell me about urself.",
        "Could you tell me about yourself?",
        "could you tell me about yourself?",
        "Would you tell me about yourself?",
        "TELL ME ABOUT YOURSELF.",
        "TELL ME ABOUT YOURSELF!",
        "TELL ME ABOUT YOURSELF?",
        "Might you tell me about yourself?",
        " Tell me about yourself?",
        " tell me about yourself?",
        " Tell me about yourself",
        " TELL ME ABOUT YOURSELF",
        "Tell me about yourself!",
        "tell me about yourself!",
        "Tell me abou yourself?",
        "Tell me about yoursef?",
    ]
}

def view_templates():
    messages = [
        {"role": "user", "content": "user1"},
        # {"role": "assistant", "content": "response1"},
        # {"role": "user", "content": "user2"},
        # {"role": "assistant", "content": "response2"},
        # {"role": "user", "content": "user3"},
        # {"role": "assistant", "content": "response3"},
    ]

    for name, template in templates.items():
        print(f"\n==== {name} ====")
        result = template.render(messages=messages, add_generation_prompt=True, eos_token="<eos>")
        print(result)
        print("-"*50)

# view_templates()
