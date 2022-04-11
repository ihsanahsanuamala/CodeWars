package CodeWars;


public class CreditCardMask {
    public static String maskify(String str){
        char[] ch = str.toCharArray();
        if (ch.length > 4){
            for (int i = 0; i < ch.length-4; i++) {
                ch[i] = '#';
            }
        }
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < ch.length; i++) {
            stringBuilder.append(ch[i]);
        }
        String joinedString = stringBuilder.toString();
        return joinedString;
    }
    
    public static void main(String[] args) {
//        String mark = "4556364607935616";
//        String mark = "";
//        char[] ch = mark.toCharArray();
////        System.out.println(ch);
//
//        if (ch.length > 4){
//            for (int i = 0; i < ch.length-4; i++) {
////                System.out.print(ch[i]);
//                ch[i] = '#';
//            }
//        }
//        System.out.println(ch);
        System.out.println(maskify("4556364607935616"));
    }
}
