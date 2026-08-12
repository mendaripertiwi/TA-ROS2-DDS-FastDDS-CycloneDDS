# TA-ROS2-DDS-FastDDS-CycloneDDS

Source code tugas akhir analisis perbandingan kinerja Fast DDS dan Cyclone DDS pada ROS2.

## Deskripsi

Repository ini berisi source code yang digunakan untuk penelitian tugas akhir mengenai perbandingan performa middleware DDS pada ROS2 menggunakan komunikasi publisher-subscriber.

Pengujian dilakukan dengan membandingkan dua middleware DDS:
- Fast DDS
- Cyclone DDS

Parameter evaluasi yang digunakan:
- Throughput
- Latency
- Packet Loss


## Environment Pengujian

- Operating System: Ubuntu 24.04.3 LTS
- Framework: ROS2 Kilted
- Bahasa Pemrograman: Python (rclpy)
- Komunikasi: Publisher-Subscriber


## Konfigurasi Pengujian

- 1 Publisher
- 4 Subscriber
- Topic: /dds_test_topic
- Message size: 1,06 KB
- Frequency: 10 Hz


## Menjalankan Fast DDS

Gunakan konfigurasi middleware Fast DDS:

```bash
source /opt/ros/kilted/setup.bash
source ~/ros2_ws/install/setup.bash

export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
unset CYCLONEDDS_URI

export ROS_DOMAIN_ID=7
export ROS_LOCALHOST_ONLY=0


```
## Menjalankan Cyclone DDS

Gunakan konfigurasi middleware Cyclone DDS:

```bash
source /opt/ros/kilted/setup.bash
source ~/ros2_ws/install/setup.bash

export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

export ROS_DOMAIN_ID=7
export ROS_LOCALHOST_ONLY=0
