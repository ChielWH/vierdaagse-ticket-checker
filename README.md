## Configure crontab

#### Step 1: configure runtime environment (venv)
Run:
```
virtualenv .venv --python=$(which python3.11)
source .venv/bin/activate
pip install -r requirements.txt
```
You can choose to use another Python version

#### Step 2: set script value
Set the `SCRIPT_DIR` value in `./script.sh` to this folder:
```
sed -i "" "s|SCRIPT_DIR=.*|SCRIPT_DIR=\"$(pwd)\"|" script.sh
```

#### Step 3: create crontab config line
Create crontab config to run the script every minute and log to this folder:
```
echo "*/1 * * * * ${PWD}/script.sh >> ${PWD}/cron.log 2>&1"
```
You can set a different schedule by replacing the `*/1 * * * *` with a different value, go to https://crontab.guru for more information on how to create a schedule.

#### Step 4: configure crontab
Copy the printed line from the previous step, run `EDITOR=nano crontab -e`, paste it in the crontab file, press CRTL+O and CRTL+X to save and exit the nano editor.