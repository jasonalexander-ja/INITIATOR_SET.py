echo "Checking for dependencies"

REQUIRED="python3"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED|grep "install ok installed")
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED. Setting up $REQUIRED."
  sudo apt-get --yes install $REQUIRED
fi

REQUIRED="python3-pyqt5"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED|grep "install ok installed")
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED. Setting up $REQUIRED."
  sudo apt-get --yes install $REQUIRED
fi

REQUIRED="pyqt5-dev-tools"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED|grep "install ok installed")
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED. Setting up $REQUIRED."
  sudo apt-get --yes install $REQUIRED
fi

REQUIRED="qttools5-dev-tools"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED|grep "install ok installed")
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED. Setting up $REQUIRED."
  sudo apt-get --yes install $REQUIRED
fi

REQUIRED="python3-pip"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED|grep "install ok installed")
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED. Setting up $REQUIRED."
  sudo apt-get --yes install $REQUIRED
fi

REQUIRED="qt-material"
PKG_OK=$(pip list | grep $REQUIRED)
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED. Setting up $REQUIRED."
  if ! foobar_loc="$(type -p "pip")" || [[ -z $foobar_loc ]]; then
    sudo pip3 install $REQUIRED
  else 
    sudo pip install $REQUIRED
  fi
fi

echo "All packages found, launching INITIATOR_SET"

python3 ./main.py
