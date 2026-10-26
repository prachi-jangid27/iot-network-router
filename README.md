# Dynamic IoT Network Routing Simulator

A Python-based project that simulates an IoT network and finds the optimal route between devices using Dijkstra's shortest-path algorithm.

## Features

* Visualizes an IoT network with six nodes.
* Calculates the minimum-latency route.
* Displays the total route latency.
* Simulates changing network latency.
* Highlights the optimal route in the network graph.

## Technologies Used

* Python
* Streamlit
* NetworkX
* Matplotlib
* Dijkstra's Algorithm

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/prachi-jangid27/iot-network-router.git
   cd iot-network-router
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python -m streamlit run app.py
   ```

4. Open the local URL displayed in the terminal.

## How It Works

The application represents IoT devices as nodes and their connections as edges. Each connection has a latency value. Dijkstra's algorithm calculates the route with the minimum total latency between the selected source and destination.

The simulation button changes link latency values to demonstrate how the optimal route can change.

## 🚀 Live Demo

**Try the application here:** [IoT Network Routing Simulator](https://iot-network-router-umjo9sxbjcuwdnajdgvnuv.streamlit.app/)


## Author

Prachi Jangid
