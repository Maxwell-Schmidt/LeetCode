class Solution {
    public boolean isValid(String s) {
        if((s.length())%2 == 1){
            return false;
        }

        String parQueue = "";

        for(int i = 0; i < s.length(); i++){
            char testPar = s.charAt(i);
            switch(testPar){
                case '(':
                    parQueue = parQueue + "(";
                    break;

                case '{':
                    parQueue = parQueue + "{";
                    break;

                case '[':
                    parQueue = parQueue + "[";
                    break;

                case ')':
                    try{
                        if(parQueue.charAt(parQueue.length()-1) != '('){
                            return false;
                        }
                    } catch(StringIndexOutOfBoundsException e){
                        return false;
                    }
                    parQueue = parQueue.substring(0,parQueue.length()-1);
                    break;

                case '}':
                    try{
                        if(parQueue.charAt(parQueue.length()-1) != '{'){
                            return false;
                        }
                    } catch(StringIndexOutOfBoundsException e){
                        return false;
                    }
                    parQueue = parQueue.substring(0,parQueue.length()-1);
                    break;

                case ']':
                    try{
                        if(parQueue.charAt(parQueue.length()-1) != '['){
                            return false;
                        }
                    } catch(StringIndexOutOfBoundsException e){
                        return false;
                    }
                    parQueue = parQueue.substring(0,parQueue.length()-1);
                    break;
                    
                default:
                    return false;
            }
        }

        if(parQueue.length() != 0){
            return false;
        }
        
        return true;
    }
}