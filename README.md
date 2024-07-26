# VEXMAN - Nmap Tool

Welcome to VEXMAN, a handy tool replicating the functionality of the widely used Network Mapper (Nmap). This project is designed to provide an intuitive and powerful way to perform various network scans, with multiple scan types and interactive prompts.

## Features 

- **Interactive User Prompts:** Guides users through the scanning process with clear prompts and input requests.
- **Multiple Scan Types:** Choose from a variety of Nmap scans, including:
  - SYN Scan
  - UDP Scan
  - TCP Connect Scan
  - SCTP INIT scan
  - TCP ACK scan
  - TCP Null Scan
  - Comprehensive Scan
- **Error Handling:** Catches and reports Nmap-specific errors as well as general exceptions, providing helpful messages.

## Getting Started

### Prerequisites

Ensure you have the following installed on your Linux system:

- Git
- Python 3
- Nmap
- colorama

### Installation

#### Clone the Repository:

Open your terminal and run the following command:
```
git clone https://github.com/VEXMAN-hacks/NMAP.git
```

#### Navigate to the Directory:

Change to the directory of the cloned repository:
```
cd NMAP
```

#### Run the Script:

Execute the script with sudo to perform network scans:
```
sudo python3 NMAP.py
```

### Making the Script Executable

#### If you prefer to run the script from anywhere on your system, follow these steps:

- **Create the NMAP.py file:**
  - Save the provided Python script to a file named NMAP.py.
  - Open the terminal and run:
```
nano NMAP.py
```
- Paste the script content into the file and save it.

#### Make the Script Executable:

Change the file permissions to make it executable:
```
chmod +x NMAP.py
```

#### Move the Script to a Directory in Your PATH:

Move the script to a directory that is in your system's PATH, such as /usr/local/bin:
```
sudo mv NMAP.py /usr/local/bin/
````

#### Run the Script:

Now, you should be able to execute the script with sudo NMAP.py from anywhere in the terminal:
```
sudo NMAP.py
```

## Usage

Once you run the script, you will be prompted to choose from a variety of scan types and provide necessary inputs.
The tool will then perform the scan and display the results.

![WhatsApp Image 2024-06-02 at 11 39 32_9ae83bb2](https://github.com/Venu00/NMAP/assets/114930220/fb1187e7-920c-4d77-9581-30c7a1863be6)

Please wait for a while as it scans all the ports.
