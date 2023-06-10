🎉🎉🎉[**一个8位二进制CPU的设计和实现**](https://www.bilibili.com/video/BV1aP4y1s7Vf/) 

[**Logic Circuit**](https://logiccircuit.org/) 

…

# CPU

…

## 半加器

| A    | B    | C    | S    |
| ---- | ---- | ---- | ---- |
| 0    | 0    | 0    | 0    |
| 0    | 1    | 0    | 1    |
| 1    | 0    | 0    | 1    |
| 1    | 1    | 1    | 0    |

$$
S = A'B+AB' \\ C = AB
$$

…

## 全加器

### 1.逻辑表出

| C_in | A    | B    | S    | C_out |
| ---- | ---- | ---- | ---- | ----- |
| 0    | 0    | 0    | 0    | 0     |
| 0    | 0    | 1    | 1    | 0     |
| 0    | 1    | 0    | 1    | 0     |
| 0    | 1    | 1    | 0    | 1     |
| 1    | 0    | 0    | 1    | 0     |
| 1    | 0    | 1    | 0    | 1     |
| 1    | 1    | 0    | 0    | 1     |
| 1    | 1    | 1    | 1    | 1     |

$$
S = C_{in}'A'B+C_{in}'AB'+C_{in}A'B'+C_{in}AB 
\\
C_{out} = C_{in}'AB+C_{in}A'B+C_{in}AB'+C_{in}AB
$$

### 2.半加器级联

![fulladder_using_halfadder](./image/fulladder_using_halfadder.png)

### 3.ROM查找表

![fulladder_using_rom](./image/fulladder_using_rom.png)

![fulladder_using_rom_data](./image/fulladder_using_rom_data.png)





## 加法器

### 1.8位二进制串行加法器

![fulladder_8bits_serial](./image/fulladder_8bits_serial.png)

## 减法器





…



…