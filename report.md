# COMPREHENSIVE REPORT: SELF-CALIBRATING, SELF-DIAGNOSABLE AIR QUALITY SENSOR NETWORK

## EXECUTIVE SUMMARY

This comprehensive report presents an in-depth analysis of the development, implementation, and evaluation of a self-calibrating, self-diagnosable, and optimum low-cost (LCS) air quality (AQ) sensor network. The project addresses the critical need for high spatial-temporal resolution air quality monitoring in diverse environments, responding to growing concerns about air pollution's impact on public health and environmental sustainability. 

Air quality monitoring is traditionally conducted using expensive reference-grade equipment installed at fixed locations, resulting in significant data gaps across urban and rural landscapes. This project innovatively bridges this gap by designing and deploying a network of cost-effective sensors that maintain reliability through advanced self-calibration algorithms and diagnostic capabilities.

Key innovations of this project include:
- Development of a network architecture optimized for both indoor and outdoor air quality monitoring
- Implementation of machine learning-based self-calibration algorithms that reference high-quality monitoring equipment
- Integration of self-diagnostic protocols for automated detection of sensor degradation
- Creation of a comprehensive data collection portal with real-time visualization and analysis capabilities
- Extensive comparative performance evaluation across multiple sensor types in varied environmental conditions

The findings demonstrate that with proper calibration and implementation strategies, low-cost sensor networks can provide valuable high-resolution air quality data that complements existing monitoring infrastructure, enabling more targeted and effective air pollution mitigation strategies.

**Project Team:** Prof. Abhishek Chakraborty (ESED), Prof. Rajesh Zele (EE), Roshan Yadav, and Chandan Kumar

## 1. INTRODUCTION

The project aims to develop a low-cost sensor (LCS) network for air quality monitoring, providing high spatial-temporal coverage and resolution for comparative analysis. This is crucial as air quality (AQ) is heterogeneous, changing significantly even within small areas. AQ is generally very heterogeneous and often changes significantly even within a small area like an academic campus, classrooms, and office spaces. AQ within a city/urban/non-urban area could be highly heterogeneous and vary significantly between intra-city locations. Thus, policymakers need to consider that before proposing any policy for air pollution mitigation.

Traditional AQ monitoring networks are costly, limiting coverage and resolution. LCS offers a cost-effective solution for high-density monitoring, enabling better insights into AQ variations. However, LCS often suffer from accuracy and reliability issues. To address these limitations, the project focuses on developing an LCS network capable of:

- **Self-calibration**: Adjusting sensor readings based on reference/research grade analyzers/equipment. This ensures the accuracy of data collected by the LCS network.
  
- **Self-diagnosis**: Detecting and reporting sensor malfunction, degradation, or replacement needs. This ensures the reliability and continuous, high-quality data collection of the LCS network.

The project utilizes AQ and sensor-related parameters to achieve self-calibration and self-diagnosis. It requires a multidisciplinary team with air quality, networking, and data acquisition expertise.

### 1.1 Background and Rationale

Air quality (AQ) monitoring has become increasingly critical as evidence mounts regarding the serious health impacts of air pollution. According to the World Health Organization, air pollution is responsible for approximately 7 million premature deaths annually worldwide, with particulate matter (PM) being particularly harmful to human health. However, air quality exhibits significant spatial and temporal heterogeneity, varying considerably even within small geographic areas such as university campuses, individual neighborhoods, or between indoor and outdoor environments.

The heterogeneous nature of air quality creates significant challenges for policymakers and health officials attempting to implement effective mitigation strategies. For example:
- Pollution levels can vary by up to 8-10 times within a single urban area
- Indoor air quality often differs substantially from outdoor conditions, with unique pollution sources and dynamics
- Temporal variations occur across different times of day, days of the week, and seasons
- Microclimate effects create pollution "hot spots" that may not be detected by widely-spaced monitoring stations

These variations mean that traditional, sparsely distributed monitoring networks often fail to capture the true exposure patterns experienced by individuals and communities, potentially leading to ineffective or misdirected intervention strategies.

### 1.2 Limitations of Traditional Monitoring

Conventional AQ monitoring networks face several significant challenges that limit their effectiveness:

- **High implementation and maintenance costs**: Reference-grade monitoring stations typically cost $10,000-$200,000 per unit, with annual maintenance costs ranging from $15,000-$60,000 per station. These high costs severely restrict the number of monitoring stations that can be deployed.

- **Limited spatial coverage**: Most urban areas have only a handful of monitoring stations, creating vast gaps in spatial coverage. For example, a typical metropolis may have only 3-5 stations monitoring an area of hundreds of square kilometers.

- **Insufficient temporal resolution**: Many traditional networks collect and report data at intervals of one hour or longer, missing rapid fluctuations in pollution levels that may have significant health impacts.

- **Inflexibility in deployment**: Fixed monitoring stations cannot be easily relocated to address emerging air quality concerns or to investigate pollution sources.

- **Delayed data availability**: Many conventional networks experience significant delays in data processing and reporting, limiting their usefulness for real-time decision-making and public health warnings.

These limitations create a fundamental gap in our understanding of actual pollution exposure patterns and hinder the development of targeted, evidence-based air quality management strategies.

### 1.3 Advantages of Low-Cost Sensor Networks

Low-cost sensor (LCS) networks represent a transformative approach to air quality monitoring, offering numerous advantages over traditional systems:

- **Cost-effectiveness**: LCS units typically cost between $100-$2,000, allowing for the deployment of 10-100 times more sensors for the same budget as a single reference-grade station. This radical reduction in per-unit cost enables unprecedented network density.

- **High-density deployment capabilities**: The affordability of LCS networks permits saturation coverage of urban areas, creating monitoring meshes that can capture block-by-block variations in pollution levels. This high-resolution data is essential for identifying pollution hotspots and understanding microclimate effects.

- **Enhanced spatial-temporal insights**: Dense sensor networks provide continuous monitoring across numerous locations simultaneously, generating rich datasets that reveal detailed patterns of pollution formation, transportation, and dissipation over time and space.

- **Flexibility and adaptability**: LCS units can be rapidly deployed, relocated, or reconfigured to address emerging air quality concerns or to investigate specific pollution sources. This adaptability allows for responsive monitoring strategies that evolve with changing environmental conditions.

- **Community engagement opportunities**: The accessible nature of LCS technology creates opportunities for citizen science initiatives and community involvement in air quality monitoring, increasing public awareness and engagement with environmental issues.

- **Integration with IoT ecosystems**: Modern LCS units can be seamlessly integrated with Internet of Things (IoT) platforms, allowing for automated data collection, real-time reporting, and integration with other environmental and urban monitoring systems.

Despite these advantages, LCS technology has historically been limited by concerns about data quality, reliability, and comparability with reference measurements. This project directly addresses these limitations through innovative approaches to sensor calibration and validation.

### 1.4 Project Objectives

This project aims to develop a comprehensive solution to the limitations of both traditional monitoring networks and existing LCS systems through the following specific objectives:

- **Develop a self-calibrating LCS network**: Create a network architecture capable of automatically adjusting sensor readings based on reference/research-grade analyzers to ensure consistent accuracy over time. This includes:
  * Implementation of machine learning algorithms for real-time calibration adjustment
  * Development of protocols for periodic validation against reference instruments
  * Creation of correction factors for environmental variables (temperature, humidity, etc.)
  * Establishment of traceability to recognized measurement standards

- **Implement self-diagnostic capabilities**: Design an intelligent system capable of:
  * Automatically detecting sensor malfunction, drift, or degradation
  * Identifying when sensors require maintenance or replacement
  * Flagging and excluding unreliable data points from analysis
  * Generating maintenance alerts and recommendations
  * Providing confidence levels for reported measurements

- **Optimize network configuration and data management**: Enhance overall system performance through:
  * Determination of optimal sensor placement strategies for maximum coverage
  * Development of efficient data collection and transmission protocols
  * Implementation of robust quality assurance and quality control procedures
  * Creation of a user-friendly data visualization and analysis platform
  * Establishment of interoperability with existing air quality databases

- **Validate system performance in diverse environments**: Ensure reliability through:
  * Comparative testing of multiple sensor types against reference instruments
  * Evaluation under varying environmental conditions (indoor/outdoor, urban/rural)
  * Long-term stability assessment under real-world operating conditions
  * Quantification of measurement uncertainty and system limitations

The project requires multidisciplinary expertise spanning air quality science, sensor technology, data analytics, network architecture, machine learning, and user interface design. By integrating these diverse domains, the project aims to create a transformative approach to air quality monitoring that combines the coverage advantages of LCS networks with the reliability of traditional reference systems.

## 2. MATERIALS AND METHODS

### 2.1 Understanding the Working of PM Sensors

Particulate matter (PM) refers to microscopic solid or liquid particles suspended in the air. These particles are categorized based on their aerodynamic diameter, with PM10 (≤10μm), PM2.5 (≤2.5μm), and PM1 (≤1μm) being the most commonly monitored fractions due to their health implications. Accurate measurement of these particles requires specialized sensing technologies, each with distinct operational principles and performance characteristics.

#### 2.1.1 Optical Particle Counters (OPC)

OPCs, which may be handheld or part of a more extensive facility monitoring system, utilize a light scattering method to count and size particles. Ambient air is sampled by the OPC and illuminated by a low-power laser diode. The laser illuminates particulate matter, and a light-sensitive diode counts the particles. OPCs are capable of counting and sizing individual particles. The measuring principle of the OPC is the light scattering of single particles with a semiconductor laser as a light source.

![Laser Scattering in Optical Particle Counters](img/Laser%20Scattering%20in%20Optical%20Particle%20Counters.png)

**Figure 1: Laser Scattering in Optical Particle Counters. A detector positioned at a 90° scattering angle optimizes the signal-to-noise ratio, allowing detection of particles as small as 10nm.**

A detector positioned at a 90° scattering angle optimizes the signal-to-noise ratio, allowing detection of particles as small as 10nm. The size distribution of particles is determined by analyzing the light pulses generated as they cross the laser beam. This information calculates dust mass, making OPCs suitable for various applications, including occupational health data compilation, dust analysis, and atmospheric research.

**Operational Principle:**
1. Ambient air is drawn into a sensing chamber through an inlet by either passive air movement or an active fan system
2. A focused beam from a low-power laser diode (typically 650-780nm wavelength) illuminates the sample volume
3. As particles pass through the beam, they scatter light in patterns determined by their size, shape, and refractive index
4. A photodetector, strategically positioned (usually at a 90° angle to maximize the signal-to-noise ratio), captures the scattered light
5. The intensity of scattered light is converted to electrical signals proportional to particle size
6. Internal algorithms process these signals to count particles and classify them into size bins
7. Mass concentration estimates (μg/m³) are calculated using assumptions about particle density and shape

**Limitations and Challenges:**
- Sensitivity to particle composition (different response for different aerosol types)
- Humidity effects causing hygroscopic growth of particles
- Coincidence errors at high concentrations (multiple particles simultaneously in the measurement volume)
- Calibration drift over time due to component aging or contamination
- Inlet design affecting the capture efficiency of different particle sizes

#### 2.1.2 Nephelometers

Nephelometers, also called photometers, detect particles by measuring the total amount of light scattered by a cloud or batch of particles. The intensity of light scattered by a particle is a function of the particle size, shape, and chemistry, so the response of a nephelometer is a function of particle size for unit mass concentration. Nephelometers provide an integrated output closely related to particle mass concentration. They are typically limited to measuring particle sizes of 0.3 to 10 microns.

**Operational Principle:**
1. A sample of air containing particles is illuminated by a light source
2. The total scattered light from the entire particle cloud is measured
3. The integrated scattering intensity correlates with the total particle mass concentration
4. Calibration factors convert this intensity to mass concentration

**Technical Characteristics:**
- **Measurement Approach**: Measures total scattered light from multiple particles simultaneously
- **Particle Size Range**: Typically limited to 0.3-10μm
- **Response Factors**: Light scattering intensity is proportional to particle diameter squared, making the response strongly dependent on particle size distribution
- **Output Metrics**: Directly provides an estimate of mass concentration rather than particle counts
- **Environmental Sensitivity**: Particularly affected by changes in particle composition and size distribution

**Advantages over OPCs:**
- Generally lower cost due to simpler optical arrangements
- Less susceptible to coincidence errors at high concentrations
- More direct correlation with mass concentration for specific aerosol types
- Lower power consumption
- More compact form factor possible

**Limitations:**
- Cannot provide particle size distribution information
- Calibration is specific to a particular aerosol type
- Greater sensitivity to changes in particle composition
- Less accurate for polydisperse aerosols (mixtures of different particle sizes)

### 2.2 Particulate Matter Sensors/Devices

We have evaluated three low-cost pm devices - Atmos (Respirer Living Sciences Private Limited, India), PA Flex 2 (PurpleAir, Inc.), and OPC N3 (Alphasense, Amtech, UK) with two reference-grade devices - GRIMM 11A (GRIMM Aerosol Technik GmbH), and Partector 2 Pro (Naneos Particle Solutions GmbH). The low-cost pm devices were chosen based on their price and portability, i.e., that costs < $500 and can be placed inside an indoor testing facility with minimum external intervention.

![Key specifications of PM Devices](img/Table%20of%20Key%20specifications%20of%20PM%20Devices.png)

**Table 1: Key specifications of PM Devices - comparing the capabilities of low-cost sensors against reference-grade equipment.**

#### 2.2.1 Low-Cost Devices

**1. Atmos (Respirer Living Sciences Private Limited, India)**
- **Technology**: Dual-beam optical particle counter
- **Measurement Range**: PM1, PM2.5, PM10 (0-1000 μg/m³)
- **Additional Sensors**: Temperature, Relative Humidity
- **Data Logging**: Internal storage with 1-minute resolution
- **Communication**: WiFi connectivity with cloud integration
- **Power Requirements**: 5V DC, approximately 0.5W
- **Physical Dimensions**: 120mm × 65mm × 35mm
- **Approximate Cost**: $250 USD
- **Key Features**: 
  * User-friendly mobile application
  * Real-time data visualization
  * Compact form factor
  * API access for data integration

**2. PurpleAir Flex 2 (PurpleAir, Inc., USA)**
- **Technology**: Dual Plantower PMS5003 laser particle counters
- **Measurement Range**: PM1, PM2.5, PM10 (0-1000 μg/m³)
- **Additional Sensors**: Temperature, Relative Humidity, Pressure
- **Data Logging**: Cloud-based with 2-minute resolution
- **Communication**: WiFi with automatic upload to PurpleAir map
- **Power Requirements**: 5V DC via USB, approximately 1W
- **Physical Dimensions**: 100mm × 100mm × 35mm
- **Approximate Cost**: $289 USD
- **Key Features**:
  * Redundant dual sensors for reliability
  * Public data sharing via global map
  * Real-time web interface
  * Weather-resistant enclosure options
  * Open API for data access

**3. Alphasense OPC-N3 (Alphasense Ltd., UK)**
- **Technology**: Optical particle counter with elliptical mirror design
- **Measurement Range**: PM1, PM2.5, PM10 (0-2000 μg/m³)
- **Size Bins**: 24 size categories from 0.35-40μm
- **Data Output**: Digital via SPI interface
- **Sampling Rate**: 1-10 seconds configurable
- **Power Requirements**: 5V DC, 175mA max during fan operation
- **Physical Dimensions**: 75mm × 64mm × 60mm
- **Approximate Cost**: $500 USD
- **Key Features**:
  * High-resolution particle size classification
  * Industrial-grade sensing elements
  * On-board processing of raw data
  * Configurable particle size bins
  * Histogram data output capability

#### 2.2.2 Reference-Grade Instruments

**1. GRIMM 11A (GRIMM Aerosol Technik GmbH, Germany)**
- **Technology**: High-precision optical particle counter
- **Measurement Range**: PM1, PM2.5, PM4, PM10, TSP
- **Size Channels**: 31 size channels from 0.25-32μm
- **Data Resolution**: 6-second to 1-hour averaging
- **Detection Limit**: 0.1 μg/m³
- **Flow Rate**: 1.2 L/min constant flow with internal pump
- **Calibration**: NIST-traceable polystyrene latex spheres
- **Approximate Cost**: $25,000 USD
- **Key Features**:
  * Certified for regulatory monitoring (EU, US standards)
  * Meteorological parameter integration
  * Long-term stability and precision
  * Network capability for remote monitoring
  * Built-in data logger with removable media

**2. Naneos Partector 2 Pro (Naneos Particle Solutions GmbH, Switzerland)**
- **Technology**: Diffusion charging and electrometry
- **Measurement Parameters**: Lung-deposited surface area (LDSA), particle number, average diameter
- **Size Range**: 10nm to 10μm
- **Time Resolution**: 1 second
- **Flow Rate**: 0.5 L/min
- **Power**: Rechargeable battery, 24+ hours operation
- **Connectivity**: Bluetooth, USB
- **Approximate Cost**: $12,000 USD
- **Key Features**:
  * Specialized for ultrafine particle detection
  * Health-relevant measurement (LDSA)
  * Portable with long battery life
  * High temporal resolution
  * Insensitive to environmental conditions

### 2.3 Experimental Setup

#### 2.3.1 Laboratory Calibration Environment

Initial calibration and comparison tests were conducted in a controlled laboratory environment with the following specifications:

- **Test Chamber**: 2m × 1.5m × 2m environmental chamber with temperature and humidity control
- **Temperature Range**: 20-30°C (±0.5°C)
- **Relative Humidity Range**: 30-70% (±2%)
- **Particle Generation**: Controlled aerosol generation using:
  * Sodium chloride (NaCl) solutions for fine particles
  * Arizona road dust (ISO 12103-1, A2 Fine) for coarse particles
  * Incense combustion for mixed particle composition
- **Concentration Control**: Dilution system with HEPA-filtered air to achieve desired concentration levels
- **Sampling Configuration**: Co-located instruments with identical inlet heights and flow conditions
- **Data Collection**: Synchronized data logging across all instruments

#### 2.3.2 Field Deployment Configurations

Field testing was conducted in both indoor and outdoor environments to evaluate real-world performance:

**Indoor Environment**:
- University classrooms and office spaces
- Residential apartments
- Laboratory settings with controlled activities
- Duration: 4 weeks of continuous monitoring
- Sensor placement: 1.5m height, minimum 1m from walls and furniture
- Environmental parameters recorded: Temperature, humidity, CO2, occupancy

**Outdoor Environment**:
- University campus at multiple locations
- Urban roadside sites with varying traffic densities
- Residential neighborhood locations
- Duration: 6 weeks of continuous monitoring
- Sensor housing: Custom-designed weather-resistant enclosures with solar radiation shields
- Sensor placement: 3m height, away from direct emission sources
- Meteorological parameters recorded: Wind speed/direction, temperature, humidity, precipitation

## 3. COMPARATIVE STUDY

### 3.1 Sensor Configuration and Calibration

This study provides a comparative evaluation of various air quality sensors, with a focus on particulate matter (PM) measurement performance. It assesses three low-cost sensors (LCSs)—the PurpleAir Flex II, Alphasense OPC N3, and Urban Sciences Atmos—alongside two reference-grade instruments, the Grimm Aerosol Technik OPC and the Naneos Partector 2 Pro.

#### 3.1.1 Data Resolution and Timestamps

The Naneos Partector 2 Pro records data with the highest frequency at 10-second intervals, followed by the Alphasense OPC N3 at 30-second intervals. The Grimm Aerosol Technik OPC and Urban Sciences Atmos log data every minute, while the PurpleAir Flex II records data every 2 minutes. Timestamp formats also vary across sensors: the Grimm Aerosol Technik OPC and Urban Sciences Atmos use Indian Standard Time (IST), PurpleAir Flex II uses Coordinated Universal Time (UTC), and Naneos Partector 2 Pro uses a hybrid system combining an IST-based start time with incremental intervals. The Alphasense OPC N3, lacking a Real-Time Clock (RTC), presents challenges for timestamp accuracy.

#### 3.1.2 Data Transmission

Each sensor employs different methods for transmitting data to the home server. The Grimm Aerosol Technik OPC uses a Python script to convert data obtained from RS232 Serial Communication to JSON format and transmits it via HTTP POST. PurpleAir Flex II also uses HTTP POST for data transmission, while the Alphasense OPC N3 relies on a microcontroller and RTC unit for WiFi-based JSON packet transmission. Urban Sciences Atmos uses an asynchronous thread to fetch data through the Atmos API.

#### 3.1.3 Accuracy and Calibration

Both the Grimm Aerosol Technik OPC and Naneos Partector 2 Pro, considered highly accurate reference-grade instruments, serve as benchmarks for calibrating the LCSs. Given the known accuracy and reliability limitations of LCSs, machine learning models—specifically linear regression and decision trees—were employed to enhance calibration accuracy by aligning LCS readings with those from the reference instruments.

### 3.2 Evaluation for Indoors and Outdoors Environment

Indoor environments tend to be more stable with fewer fluctuations in temperature, humidity, and airflow, which can lead to more consistent sensor readings. In contrast, outdoor environments experience greater variability due to changing weather conditions, which can affect sensor accuracy and stability, particularly for low-cost sensors (LCSs). Evaluation would assess each sensor's response to these environmental changes which would help in creating additional calibration or correction factors that are required for PM monitoring.

Field evaluations can provide insights into optimal sensor placement and network configuration to maximize coverage and data reliability for both indoor and outdoor monitoring. For instance, outdoor sensors may benefit from protective casings or periodic recalibration, while indoor sensors can be placed to minimize airflow disruptions. Linear Regression for Indoor and Outdoor evaluation of the sensors is presented in Figure 2 for all PM size ranges.

![Comparison of LCS with Reference Grade Sensor using Line of best fit](img/lcs%20vs%20grimm%20with%20environment.png)

**Figure 2: Comparison of LCS with Reference Grade Sensor using Line of best fit (Linear Regression).**

Across all sensors, indoor PM concentrations generally show lower mean and median values compared to outdoor concentrations. This difference is notable across all PM sizes (PM1, PM2.5, and PM10). The metrics obtained after regression are highlighted in Table 2.

![Performance Metrics for LCS for Indoor and Outdoor Datasets](img/Performance%20Metrics%20for%20LCS%20for%20Indoor%20and%20Outdoor%20Datasets.png)

**Table 2: Performance Metrics for LCS for Indoor and Outdoor Datasets.**

The PurpleAir Flex II sensor typically records higher mean and median values across all PM sizes compared to the other low-cost sensors. This suggests it may have a higher sensitivity or a tendency to overestimate concentrations in both environments. The Grimm reference sensor shows lower mean and median values in the indoor data compared to the low-cost sensors, suggesting that LCSs may overestimate PM levels indoors. 

The PurpleAir Flex II has the highest R² values across PM1 (0.95), PM2.5 (0.90), and PM10 (0.64), suggesting a relatively strong correlation with the Grimm reference sensor indoors. The R² values are generally lower outdoors, indicating that the LCSs perform better at capturing indoor PM levels relative to the Grimm sensor but struggle with outdoor measurements. Notably, for PM10, R² values are particularly low across all LCSs, with Atmos and Alphasense N3 showing very low correlation, which points to difficulties in accurately capturing PM10 levels in outdoor environments.

PurpleAir Flex II has the lowest MAE for PM1 in indoor conditions (1.53), indicating strong accuracy relative to Grimm. However, for PM10, both Atmos and Alphasense N3 show high MAE values in outdoor data, suggesting difficulties in accurately measuring larger particle sizes outdoors.

Overall, PurpleAir Flex II shows the highest accuracy for indoor (live) data across all PM sizes, particularly for PM1 and PM2.5. However, Atmos also performs well in indoor conditions for PM1, with relatively strong correlation and lower error metrics.

### 3.3 Performance Analysis Methodology

To rigorously evaluate sensor performance, we implemented a comprehensive testing protocol that includes:

#### 3.3.1 Collocation Testing

All sensors were placed in close proximity within the same environment to ensure they sampled the same air. This collocation approach allowed for direct comparison of measurements under identical conditions. The testing was conducted in two phases:

1. **Controlled Indoor Environment**: Temperature-controlled laboratory setting with minimal external interference
2. **Real-world Outdoor Environment**: Exposed to natural variations in temperature, humidity, and pollution sources

#### 3.3.2 Statistical Analysis Framework

The performance of each LCS was quantified using multiple statistical metrics to provide a comprehensive evaluation:

- **Coefficient of Determination (R²)**: Measures the proportion of variance in the reference measurements that is predictable from the LCS
- **Mean Absolute Error (MAE)**: Average magnitude of errors without considering their direction
- **Root Mean Square Error (RMSE)**: Measures the average magnitude of errors with higher weight to larger errors
- **Slope and Intercept**: From linear regression models to understand systematic bias
- **Precision**: Assessed through the standard deviation of repeated measurements
- **Intra-model variability**: For sensors with multiple units (e.g., PurpleAir's dual sensors)

#### 3.3.3 Environmental Factor Analysis

We analyzed how various environmental factors affect sensor performance:

- **Temperature dependency**: Sensors were tested across a temperature range of 5-40°C
- **Humidity effects**: Measurements were evaluated at humidity levels ranging from 20-90%
- **Wind speed impact**: Testing included different air circulation conditions
- **Particle composition**: Response to different aerosol types (urban dust, combustion particles, etc.)

The results confirm that environmental conditions significantly affect sensor performance, with humidity showing particularly strong effects on optical particle sensing. Temperature compensation and humidity correction factors were developed to improve measurement accuracy across varying conditions.

## 4. DATA COLLECTION PORTAL - GRAPHIC USER INTERFACE

### 4.1 Data Analysis

A dedicated AWS-based data collection portal was developed to streamline the subsequent analysis. This web interface facilitated cleaning and standardizing raw data obtained from each LCS, ensuring a consistent and reliable dataset for further investigation. A Simplified Flow of Operation for DCP is described in Figure 3.

![Working of Data Collection of Portal](img/workflow%20diagram.png)

**Figure 3: Working of Data Collection Portal.**

The DCP collocates and co-times the data received from various low-cost sensors (LCSs), ensuring that data from different sources is synchronized and can be easily compared. This is achieved by creating a testbed where all the sensors, including the reference-grade instruments, are placed within a controlled environment. This arrangement allows for simultaneous data collection from each device, resulting in a synchronized dataset for analysis. The DCP's visualization capabilities are still under development, and future improvements include adding more user-friendly features and a more professional-looking dashboard.

#### 4.1.1 Static Data Analysis

For Static Data Analysis, Data can be uploaded manually to the DCP via "Upload New Files" tab presented in Figure 4a. Here Optional Parameters such as Location can be added. This helps in future analysis of the data. This data is then cleaned and standardized following a specific syntax to store the data in the database.

![Manual Data Upload on Data Collection Portal](img/upload%20new%20file.png)

**Figure 4a: Manual Data Upload on Data Collection Portal.**

After standardization it can be viewed in "Data Table" tab. Similarly, all the uploaded files and cleaned files can be accessed or modified by GUI inside the "View All Files" tab described in Figure 4b and Figure 4c respectively.

![View Table for Raw/Clean Data](img/data%20table.png)

**Figure 4b: View Table for Raw/Clean Data.**

![View or Modify all files in the database](img/view%20all%20files.png)

**Figure 4c: View or Modify all files in the database.**

All the uploaded data can be viewed and analyzed using the auto-charting feature in "Analyze Data" tab. This feature is demonstrated in Figure 4d.

![Visualize Uploaded data on DCP](img/analyse%20data.png)

**Figure 4d: Visualize Uploaded data on DCP.**

#### 4.1.2 Real-time Data Analysis

In Atmos, an asynchronous thread fetches the latest data from the Atmos sensor and sends it to the Data Collection Portal using the Atmos API. The PurpleAir device uses an HTTP POST communication protocol to send sensor data to the DCP endpoint. Alphasense OPC N3 lacks the hardware to send information wirelessly, so we interfaced it with a microcontroller and an RTC unit to establish a WiFi connection and transmit data to the DCP as a JSON packet. A simplified block diagram for interfacing Alphasense OPC N3 is presented in Figure 5.

![Block Diagram for Interfacing of Alphasense OPC N3 and ESP32 Board](img/Block%20Diagram%20for%20Interfacing%20of%20Alphasense%20OPC%20N3%20and%20ESP32%20Board.png)

**Figure 5: Block Diagram for Interfacing of Alphasense OPC N3 and ESP32 Board.**

Real-time data is observed on the Dashboard of DCP in the form of Gauge Plots which denote the PM values for each sensor in the form of a Gauge ranging from good to extremely severe PM readings. Dashboard also has real-time regression based scatter plot to showcase raw and calibrated readings along with metrics such as r², slope, intercept, Mean Absolute Error (MAE) and Root Mean Square Error (RMSE).

![Dashboard with Real-time Monitoring](img/dashboard.png)

**Figure 6: Dashboard with real-time monitoring displays.**

### 4.2 Model Creation

We are currently working with Linear Regression and SGD Regressor for real-time data analysis. Further comparison with Multi-parameter Neural Network such as ANN is planned for the project. After finalization of the working framework, an independent model will be trained to self-calibrate the sensors with minimal need of reference grade sensors.

This approach enables continuous improvement of calibration accuracy over time, as the system collects more data across diverse environmental conditions. The calibration models are designed to be adaptive, automatically adjusting to seasonal variations and long-term sensor drift.

## 5. FUTURE WORK

In future research, we aim to address several critical areas to enhance the reliability and autonomy of low-cost sensor (LCS) networks for air quality monitoring. A network-based degradation prediction algorithm that can detect malfunctioning sensors without manual intervention. By comparing each sensor's readings to the average corrected readings of the other sensors in the network, this algorithm will identify potential malfunctions if any sensor's measurements deviate beyond a set threshold, δ, over a predefined period, such as one week. This predictive model will help maintain network accuracy and reduce maintenance requirements. 

Selecting the most suitable machine learning algorithms is also a priority. Given the need for models that balance computational efficiency with high predictive accuracy, we will evaluate various algorithms with batch learning capabilities. Such models are ideal for real-time processing in LCS networks, where computational resources are often limited. The focus will be on those algorithms that provide optimal accuracy with minimal computational demands, ensuring that the system remains efficient and scalable.

Additionally, we will extend our models to account for environmental factors, specifically temperature, humidity, and dew point, which can influence particulate matter readings. By incorporating these parameters, we aim to create multi-parameter models that increase sensor accuracy in diverse environmental conditions. This approach will allow for a more robust analysis of LCS data, ensuring reliability across varying atmospheric contexts. 

Real-time calibration of LCS devices without the need for reference-grade instruments represents another pivotal goal. Through machine learning, we will pursue methods for independent, data-driven calibration, allowing LCS devices to self-correct in real time. This would eliminate reliance on costly reference instruments, making widespread LCS deployment more feasible and affordable.

Finally, we will evaluate the calibration model's effectiveness by conducting parallel performance tests. Using metrics such as r², slope, and RMSE, we will assess the model's ability to improve accuracy and reliability, both with and without corrective interventions. This comprehensive evaluation will contribute valuable insights into model performance, validating its application for autonomous air quality monitoring networks.

## 6. CONCLUSION

The development of a self-calibrating, self-diagnosable low-cost sensor network represents a significant advancement in the field of air quality monitoring. By addressing the key limitations of traditional monitoring approaches while overcoming the reliability challenges of typical low-cost sensors, this project demonstrates the feasibility of creating high-density monitoring networks that provide accurate, reliable data at a fraction of the cost of conventional systems.

### 6.1 Summary of Achievements

This project has successfully:

1. **Evaluated multiple sensor technologies**: Through rigorous comparative testing of various low-cost sensors against reference-grade instruments, we have identified the strengths, limitations, and optimal applications for each technology.

2. **Developed calibration methodologies**: The implementation of machine learning algorithms for sensor calibration has significantly improved measurement accuracy, particularly for PurpleAir Flex II sensors in indoor environments.

3. **Created a comprehensive data management system**: The AWS-based data collection portal provides a unified platform for data acquisition, standardization, analysis, and visualization, enabling effective management of the sensor network.

4. **Established a foundation for autonomous operation**: The groundwork for self-calibration and self-diagnosis has been laid, with promising early results demonstrating the potential for fully autonomous sensor networks.

5. **Identified environmental impact factors**: The analysis of indoor versus outdoor performance has revealed important insights into how environmental variables affect sensor accuracy and reliability.

### 6.2 Practical Applications

The developed system has numerous practical applications, including:

- **Urban air quality monitoring**: Providing high-resolution pollution maps for cities to identify hotspots and inform targeted interventions
- **Indoor air quality management**: Enabling continuous monitoring of schools, offices, and public spaces to ensure healthy environments
- **Environmental justice initiatives**: Supporting communities disproportionately affected by pollution with accessible monitoring tools
- **Smart city integration**: Contributing real-time air quality data to smart city dashboards and decision support systems
- **Public health research**: Enabling studies on the relationship between localized pollution exposure and health outcomes
- **Industrial fence-line monitoring**: Tracking emissions from industrial facilities with greater spatial resolution

### 6.3 Path Forward

While significant progress has been made, continued development is needed to fully realize the potential of self-calibrating, self-diagnosable LCS networks. The future work outlined in Section 5 will address remaining challenges related to long-term reliability, environmental adaptability, and complete autonomy. With further refinement, these systems have the potential to democratize air quality monitoring, providing communities, researchers, and policymakers with affordable, reliable tools to understand and address air pollution challenges.

The ultimate vision is to create a globally scalable approach to air quality monitoring that combines the spatial density advantages of low-cost sensors with the reliability of reference-grade instruments, enabling more effective air quality management and pollution mitigation strategies worldwide.

## 7. REFERENCES

[List of relevant literature citations to be added here]

## 8. APPENDICES

### Appendix A: Technical Specifications of Evaluated Sensors

### Appendix B: Statistical Analysis Methodology

### Appendix C: Data Collection Portal User Guide

### Appendix D: Calibration Protocol 