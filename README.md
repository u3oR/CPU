Reference🎉:[**一个8位二进制CPU的设计和实现**](https://www.bilibili.com/video/BV1aP4y1s7Vf/) 

Software:[**Logic Circuit**](https://logiccircuit.org/) 

<p align = "center">
	<img alt="CPU" src="./image/CPU.png" height="300px" width="300px">
</p>

# 一只8位CPU的诞生(simulation)

…

## 半加器

| A    | B    | C    | S    |
| ---- | ---- | ---- | ---- |
| 0    | 0    | 0    | 0    |
| 0    | 1    | 0    | 1    |
| 1    | 0    | 0    | 1    |
| 1    | 1    | 1    | 0    |

$$
S = A'B+AB' 
$$

$$
C = AB
$$

…

![halfadder](./image/halfadder.png) 

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
$$

$$
C_{out} = C_{in}'AB+C_{in}A'B+C_{in}AB'+C_{in}AB
$$

略…

### 2.半加器级联

![fulladder_using_halfadder](./image/fulladder_using_halfadder.png)

### 3.ROM查找表

![fulladder_using_rom](./image/fulladder_using_rom.png)

利用上面的逻辑表出式可以得出下面的查找表：


$$
地址:C_{in}*4 + A * 2 * B ,数据： S * 2 + C_{out}
$$


![fulladder_using_rom_data](./image/fulladder_using_rom_data.png)





## 加法器

### 8位二进制串行加法器

![fulladder_8bits_serial](./image/fulladder_8bits_serial.png)

### 测试电路

![adder_8bit_test_circuit](./image/adder_8bit_test_circuit.png)

## 减法器

由加法器的特性可以知道：1 + 255 = 0, 3+255 = 2 **(忽略进位)**，这意味着对应8位的无符号数 +255 和 -1 是等价的。

同理 5 + 254 = 5 + 255 - 1 = (5 + 255) - 1 = 4 - 1 = 3，这就意味着+254和 -2 是等价的。

在二进制表示中 255和0是互相按位取反的，254和1是互相按位取反的。那么

3 - 1 = 3 + 255 = 3 + **254** +1 ==>> 3 + **~1** + 1 (‘~x’的意思是对x取反) 

3 - 1 = 3 + (~1 + 1)，**(~1 + 1)就是-1的补码 ** 

利用加法器和溢出的特性进行减法运算

我们要做出减法器实现 A-B，就要先求出 -B的补码C 再做A+C就可以完成运算了。

…

先实现一个取反器，

![reverser_8bit_circuit](./image/reverser_8bit_circuit.png)

**EN** 0:不取反 1:取反

![add_sub_8bit_circuit](./image/add_sub_8bit_circuit.png)

…

## 数码管

### HEX数码管

circuit

![seg_hex_circuit](./image/seg_hex_circuit.png)

rom

![seg_hex_rom](./image/seg_hex_rom.png)

…

### 单字节数码管

![seg_byte_circuit](./image/seg_byte_circuit.png)

### 单字节十进制数码管

…

![seg_byte2dec_circuit](./image/seg_byte2dec_circuit.png)

… 

![seg_byte2dec_rom](./image/seg_byte2dec_rom.png)

…

```python
import os

if __name__ == '__main__':

    dirname = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(dirname, 'hex2dec_rom.bin'), 'wb') as f:
        for i in range(256):
            var = int(str(i), base=16)
            byte = var.to_bytes(length=2, byteorder='little');
            f.write(byte)
    f.close()
    print('completed!')
```

…

## RS触发器

![RS](./image/RS.png) 

| R    | S    | Q    | Q’   |
| ---- | ---- | ---- | ---- |
| 0    | 0    | Q    | Q’   |
| 1    | 0    | 0    | 1    |
| 0    | 1    | 1    | 0    |
| 1    | 1    | 0    | 0    |

## D触发器

![D](./image/D.png)

## D边缘触发器

![D_edge](./image/D_edge.png)

## T触发器

![T](./image/T.PNG)

## 3-8译码器

…

<p align = "center">
	<img alt="decoder3to8_expression" src="./image/decoder3to8_expression.png">
</p>

…

![decoder3to8](./image/decoder3to8.png)

## 存储器

![Register_8x1](./image/Register_8x1.png)

测试电路

![Register_8x1_test](./image/Register_8x1_test.png)

… 

## 存储器扩展

​	位扩展和字扩展是指将存储器中的数据在位数或字节方面进行扩展，以适应不同的数据存储需求。**位扩展**是在存储器中增加位数，使之可以存储更大的数据；而**字扩展**是在存储器中增加字节数，以提高数据处理速度和效率。

​	位扩展可以通过将存储器中的数据进行零扩展或符号扩展实现。零扩展是指在数据的高位添加0，而符号扩展是指在数据的高位添加符号位，以保持数据的符号不变。

​	字扩展可以通过将存储器中的数据进行字节拼接实现。字节拼接可以将多个字节拼接在一起形成更大的数据。

​	通过位扩展和字扩展，我们可以将存储器中的数据进行适当的扩展，以满足不同的数据处理需求。这为8位CPU设计提供了更大的灵活性和扩展性。

### 字扩展

#### 高位

![Register16x8Byte_H](./image/Register16x8Byte_H.png)

#### 低位

![Register16x8Byte_L](./image/Register16x8Byte_L.png)

### 位扩展

![Register8x16Byte](./image/Register8x16Byte.png)
