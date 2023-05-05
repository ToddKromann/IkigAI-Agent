import os

# Create the main directory for IkigAI-Agent
main_dir = 'IkigAI-Agent'
os.makedirs(main_dir, exist_ok=True)

# Create the agents subdirectory
agents_dir = os.path.join(main_dir, 'agents')
os.makedirs(agents_dir, exist_ok=True)

# Create agent_manager.py file
with open(os.path.join(main_dir, 'agent_manager.py'), 'w') as f:
    f.write('# Agent Manager\n')

# Create agent_registry.json file
with open(os.path.join(main_dir, 'agent_registry.json'), 'w') as f:
    f.write('{\n  "agent_registry": []\n}\n')

# Create README.md file
with open(os.path.join(main_dir, 'README.md'), 'w') as f:
    f.write('# IkigAI-Agent\n')

# Create .gitignore file
with open(os.path.join(main_dir, '.gitignore'), 'w') as f:
    f.write('__pycache__/\n*.pyc\n*.pyo\n*.pyd\n')

# Create agent files in the agents subdirectory
agent_files = [
    'chatgpt_agent.py',
    'zeroshotreact_agent.py',
    'reactdocstore_agent.py',
    'selfaskwithsearch_agent.py',
    'conversationalreact_agent.py'
    # (additional agents...)
]

for agent_file in agent_files:
    with open(os.path.join(agents_dir, agent_file), 'w') as f:
        f.write(f'# {agent_file}\n')

print('IkigAI-Agent directory structure created successfully!')
