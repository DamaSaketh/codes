class Palindromecheck {
    public static void main(String[] args) {
        String text ="madams";
        String reversed = new StringBuilder(text).reverse().toString();

        if (text.equals(reversed)){
            System.out.println("palindrome");
        }else {
            System.err.println("not a palindrome");
        }

    }    
    }

