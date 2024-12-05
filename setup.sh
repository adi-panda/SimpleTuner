sudo apt update
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt -y install python3.11 python3.11-venv
python3.11 -m venv .venv
source .venv/bin/activate
pip install -U poetry pip
poetry config virtualenvs.create false
poetry install

wandb login "d15bbc3c114681afe5cc0516bdaedf2700e39b68"
huggingface-cli login --token "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"

# nohup python -u train.py > train.log 2>&1 &
