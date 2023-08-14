#!bin/bash

_GREEN='\e[32m'
_NORMAL='\e[0m'
_BOLD='\e[33m'
_RED='\e[31m'
_Yellow="\033[0;36m"
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Red="\033[0;31m"          # Red

CHOOSE=0

echo -e "${_BOLD}--------------------------${_NORMAL}"
echo -e "${_Yellow} start update the config files! ${_NORMAL}"
echo -e "${_BOLD}--------------------------${_NORMAL}"
echo -e "${_Yellow} 1.update nav yaml${_NORMAL}"
echo -e "${Blue} 2.edit traffic building file${_NORMAL}"
echo -e "${Purple} 3. init config workspace${_NORMAL}"
echo -e "${Red} 4.  ${_NORMAL}"
echo -e "${_GREEN} 5.  ${_NORMAL}"
echo -e "${_BOLD}--------------------------${_NORMAL}"
echo -n "Your chose(1-6):"

function regenerate_nav_yaml()
{
	rm -r nav &&
	 
	echo -e "${_GREEN} delete old nav yaml success ${_NORMAL}"

	ros2 run rmf_building_map_tools building_map_generator nav rmf.building.yaml nav

	echo -e "${_GREEN} generate new nav yaml success ${_NORMAL}"
}

function edit_traffic_editor()
{
	taffic-editor rmf.building.yaml
}

function create_new()
{
	touch rmf.building.yaml &&
	mkdir nav &&
	touch nav/0.yaml &&
	traffic-editor rmf.building.yaml
}
read CHOOSE

case "${CHOOSE}" in
    1)
    regenerate_nav_yaml
    ;;
    2)
    edit_traffic_editor
    ;;
    3)
    create_new
    ;;
esac
echo -e "${_GREEN} comlete all progress! ${_NORMAL}"  
