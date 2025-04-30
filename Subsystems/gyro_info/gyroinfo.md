This is the page for a brief information regarding the current IMU of GWEN

IMU module: MPU6050
IMU slave address: 0x68 | 0x69 (depending on if its a reset HIGH or LOW)

The IMU contains three different sensors:
1) Temperature 
    unit: Degree Celcius
    range: -40 to +85
    calibration: raw_data / 340
2) Gyroscope
    unit: degree/s
    range: +-250
    calibration: raw_data / 131
3) Acceleration
    unit: g
    range: +- 2
    calibration: raw_data / 16384
    *NOTE: acceleration on the z plane will always be 1g, because of gravity
more information regarding the sensor calibration is available under the datasheet



