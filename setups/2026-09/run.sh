set -e

docDir="/home/$USER/Documents"
modDir="$docDir/midimodulator"
drumDir="$docDir/electronicdrums"

thruCmd="cd $modDir/thru; bash"
modCmd="cd $modDir/modulator; bash"

tmuxCmds=()
tmuxCmds+=("tmux new-session \"htop\"\;")
tmuxCmds+=("split-window -h \"$thruCmd\"\;")
tmuxCmds+=("select-pane -t 0 \; split-window -v -l '80%' \"cd $drumDir/py; bash\"\;")
tmuxCmds+=("select-pane -t 1 \; split-window -v -l '50%' \"cd $drumDir/setups; bash\"\;")

cmds=${#tmuxCmds[@]}
topRightPane=$((cmds-1))

tmuxCmds+=("send-keys -t 1 \"./upload.py\"\;")
tmuxCmds+=("send-keys -t 2 \"./note_monitor.sh\" ENTER\;")
tmuxCmds+=("select-pane -t $topRightPane \; split-window -v -l '50%' \"$modCmd\"\;")
tmuxCmds+=("send-keys -t $((topRightPane+1)) \"cargo run\" ENTER\;")
tmuxCmds+=("select-pane -t $topRightPane")


cmdf=$(mktemp)
echo "${tmuxCmds[@]}" > $cmdf
chmod +x $cmdf
trap "rm $cmdf" EXIT
$cmdf
