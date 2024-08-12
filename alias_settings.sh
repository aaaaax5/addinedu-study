# argcomplete for ros2 & colcon
alias tmp1="eval \"\$(register-python-argcomplete3 ros2)\""
alias tmp2="tmp1; eval \"\$(register-python-argcomplete3 colcon)\""

# ALIAS settings
ID=49

alias sauu="sudo apt update && sudo apt upgrade"
alias ea="subl ~/.alias_setting.sh; echo \"edit alias setting\""
alias ros2study="humble; source /home/hj/ros2_study/install/local_setup.bash; echo \"ros2_study workspace is activated.\""
alias killgazebo='killall -9 gazebo & killall -9 gzserver & killall -9 gzclient'

alias sz="source ~/.zshrc; echo \"Zshrc is reloaded!\""
alias sb="source ~/.bashrc; echo \"Bashrc is reloaded!\""

alias ros_domain="export ROS_DOMAIN_ID=\$ID; echo \"ROS_DOMAINID is set to \$ID !\""
alias humble="source /opt/ros/humble/setup.bash; ros_domain; echo \"ROS2 Humble is activated\""

ws_setting()
{
	humble
	source ~/$1/install/local_setup.bash
	echo "$1 workspace is activated."
	tmp2
}

alias  ros2_study="ws_setting \"ros2_study\""
