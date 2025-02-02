# def xor(a,b) :
    
#     res = ""
#     for i in range(len(b)) :
#         if a[i] == b[i] :
#             res += "0"
#         else :
#             res += "1"
            
#     return res 

# # result = xor('0100','0011')
# # print(result)

# def crc_remainder( data , divisor ) :
    
#     padded_data = data + '0' * (len(divisor ) - 1)
    
#     remainder = padded_data[:len(divisor)]
    
#     for i in range(len(data)) :
#         if remainder[0]  == '1' :
#             remainder = xor(remainder , divisor)
            
#         else :
#             remainder = xor(remainder , '0' * len(divisor))
            
#         if i + len(remainder) < len(padded_data) :
#             remainder  = remainder[1:] + padded_data[i + len(divisor)]
#         else :
#             remainder = remainder[1:]
            
        
#     return remainder 


# def crc_check(data_with_crc , divisor) :
#     remainder = crc_remainder(data_with_crc , divisor)
#     return remainder == '0' * (len(divisor) - 1)
  
# data = input(" Enter the data : ")
# divisor = input(" Enter the divident : ")

# crc = crc_remainder(data, divisor)
# print(f"CRC for the data {data} is: {crc}")  

# data_with_crc = data + crc

# is_error_free = crc_check(data_with_crc, divisor)
# print(f"Data is error-free: {is_error_free}")
        
    
    
    
import random

def xor(a, b):
    res = ""
    for i in range(len(b)):
        res += '0' if a[i] == b[i] else '1'
    return res

def crc_remainder(data, divisor):
    padded_data = data + '0' * (len(divisor) - 1)  # Append zeros
    remainder = padded_data[:len(divisor)]  # Initialize remainder
    
    for i in range(len(data)):
        if remainder[0] == '1':
            remainder = xor(remainder, divisor)
        else:
            remainder = xor(remainder, '0' * len(divisor))
        
        if i + len(divisor) < len(padded_data):
            remainder = remainder[1:] + padded_data[i + len(divisor)]
        else:
            remainder = remainder[1:]
    
    return remainder

def crc_check(data_with_crc, divisor):
    remainder = crc_remainder(data_with_crc, divisor)
    return remainder == '0' * (len(divisor) - 1)

def simulate_transmission(data_with_crc, error_indices):
    data_list = list(data_with_crc)
    for index in error_indices:
        data_list[index] = '1' if data_list[index] == '0' else '0'
    return ''.join(data_list)

# User inputs
data = input("Enter the data: ")
divisor = input("Enter the divisor: ")

# Generate CRC
crc = crc_remainder(data, divisor)
print(f"CRC for the data {data} is: {crc}")

# Append CRC to data
data_with_crc = data + crc
print(f"Data with CRC to be transmitted: {data_with_crc}")

# Simulate transmission errors
num_errors = int(input("Enter the number of errors to introduce: "))
error_indices = random.sample(range(len(data_with_crc)), min(num_errors, len(data_with_crc)))
transmitted_data = simulate_transmission(data_with_crc, error_indices)
print(f"Transmitted data with simulated errors: {transmitted_data}")

# Check for errors
is_error_free = crc_check(transmitted_data, divisor)
print(f"Received data is error-free: {is_error_free}")
