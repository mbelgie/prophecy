# bash script for code setup
SCRIPT_PATH=`realpath $0`
SCRIPT_DIR=`dirname ${SCRIPT_PATH}`
EXTRAS_DIR=${SCRIPT_DIR}/extras
DATA_DIR=${SCRIPT_DIR}/data
LOGS_DIR=${DATA_DIR}/logs

echo "Installing yfinance..."
pip3 install yfinance

echo "Installing matplotlib..."
pip3 install matplotlib

echo "Creating directories..."
mkdir -p ${EXTRAS_DIR}
mkdir -p ${DATA_DIR}
mkdir -p ${LOGS_DIR}
