def ddm_convert(x: float, y: float) -> list[str]:
        def calculate_minutes(x: float) -> str:
            x_minutes = round((x - int(x))* 60, 6)
            x_minutes_str = str(x_minutes)
            if x_minutes < 10:
                x_minutes_str = "0" + x_minutes_str
            if int(x_minutes) == 0:
                x_minutes_str = "0" + x_minutes_str
            return x_minutes_str 
        
        def calculate_decimal(x: float) -> str:
            dec_x = int(x)
            if dec_x == 0:
                return "00"
            if dec_x < 10:
                return "0" + str(dec_x)
            return str(dec_x)

        minus_y = ",E" if y > 0 else ",W"
        minus_x = ",N" if x > 0 else ",S"
        x = abs(x) % 100
        y = abs(y) % 1000
        str_x = calculate_decimal(x) + calculate_minutes(x) + minus_x
        str_y = calculate_decimal(y) + calculate_minutes(y) + minus_y
        if len(str_y[:str_y.find('.')]) == 4:
            str_y = "0" + str_y

        return [str_x, str_y]