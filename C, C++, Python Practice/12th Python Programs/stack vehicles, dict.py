def push(vehicle, stack):
    for c, m in vehicle.items():
        if m.lower()=="tata":
            stack.append(c)
    return stack
vehicle={"Santro":"Hyundai","Nexon":"Tata","Safari":"Tata"}
stack=[]
stack=push(vehicle,stack)
print(stack)
