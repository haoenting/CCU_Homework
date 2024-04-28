public class HugeInteger {
    private int digits[]; // the first digit is the smallest digit
    private int selfLength;
    private boolean isPositive;

    public HugeInteger() {
        digits = new int[40];
        selfLength = 0;
        isPositive = true;
    }

    // extracts the digits from a string
    public void parse(String s){
        StringBuilder MyString = new StringBuilder(s);

        if(s.charAt(0) == '-'){
            isPositive = false;
            MyString = MyString.deleteCharAt(0);
        }

        selfLength = MyString.length();
        for (int i = 0; i < selfLength; i++){
            digits[i] = MyString.charAt(selfLength - i - 1) - '0';
        }
    }

    // converts the digits to a string
    public String toString(){
        StringBuilder sb = new StringBuilder(); 
        if(!isPositive)
            sb.append('-');

        for (int i = selfLength - 1; i >= 0; i--) 
            sb.append(digits[i]);
        return sb.toString();
    }

    public void add(String s){
        StringBuilder AddString = new StringBuilder(s);

        int addLength  = AddString.length();
        int[] adder = new int[addLength];
        for (int i = 0; i < selfLength; i++){
            adder[i] = AddString.charAt(selfLength - i - 1) - '0';
        }

        for (int i = 0; i < selfLength; i++) {
            digits[i] += adder[i];
            if(digits[i] >= 10){
                digits[i] -= 10;
                digits[i + 1] += 1;
            }
        }
        if(digits[selfLength]!= 0)
            selfLength++;
    }
    public void subtract(String s){
        StringBuilder SubString = new StringBuilder(s);

        int subLength  = SubString.length();
        int[] subber = new int[subLength];
        for (int i = 0; i < subLength; i++){
            subber[i] = SubString.charAt(selfLength - i - 1) - '0';
        }

        for (int i = 0; i < selfLength; i++) {
            digits[i] -= subber[i];
            if(digits[i] < 0){
                digits[i] += 10;
                digits[i + 1] -= 1;
            }
        }
        for(int i = selfLength - 1; i >= 0 ; i--){
            if(digits[i] == 0)
                selfLength--;
            
            else break;
        }
        if(selfLength == 0)
            selfLength++;
    }

    public boolean isEqualTo(HugeInteger other) {
        boolean result = true;
        if(isPositive != other.isPositive)
            result = false;
        else if(selfLength != other.selfLength)
           result = false;
        else{
            for(int i = 0; i < selfLength; i++){
                if(digits[i] != other.digits[i]){
                    result = false;
                    break;
                }
            }
        }
        return result;
    }
    public boolean isNotEqualTo(HugeInteger other){
        boolean result = true;
        if(isPositive != other.isPositive)
            result = false;
        else if(selfLength != other.selfLength)
           result = false;
        else{
            for(int i = 0; i < selfLength; i++){
                if(digits[i] != other.digits[i]){
                    result = false;
                    break;
                }
            }
        }
        return !result;
    }
    public boolean isGreaterThan(HugeInteger other){
        if(selfLength < other.selfLength) // self is smaller than other
           return false;
        else if(selfLength > other.selfLength) // self is longer than other
            return true;
        else{
            for(int i = selfLength -1; i >=0 ; i--){
                if(digits[i] > other.digits[i]){
                    return true;
                }
            }
        }
        return false;
    }
    public boolean isLessThan(HugeInteger other){
        if(selfLength < other.selfLength) // self is smaller than other
           return true;
        else if(selfLength > other.selfLength) // self is longer than other
            return false;
        else{
            for(int i = selfLength -1; i >=0 ; i--){
                if(digits[i] < other.digits[i]){
                    return true;
                }
            }
        }
        return false;
    }

    public boolean isGreaterTheanOrEqualTo(HugeInteger other){
        if(selfLength < other.selfLength)
            return false;
        else{
            for(int i = selfLength -1; i >=0 ; i--){
                if(digits[i] < other.digits[i]){
                    return false;
                }
            }
        }
        return true;
    }
    public boolean isLessThanOrEqualTo(HugeInteger other){
        if(selfLength > other.selfLength)
            return false;
        else{
            for(int i = selfLength -1; i >=0 ; i--){
                if(digits[i] > other.digits[i]){
                    return false;
                }
            }
        }
        return true;
    }
    public boolean isZero(){
        if(selfLength == 1 && digits[0] == 0)
            return true;
        else return false;
    }
}
