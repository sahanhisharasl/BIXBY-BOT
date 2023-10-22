if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/DX-MODS/BIXBY-BOT.git /BIXBY-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /BIXBY-BOT
fi
cd /BIXBY-BOT
pip3 install -U -r requirements.txt
echo "Starting Bixby Bot...."
python3 bot.py
