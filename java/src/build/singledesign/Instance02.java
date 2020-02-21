package build.singledesign;

/**
 * 错误的方法,如果只是使用一个内部成员变量,调用自身会出现迭代死循环
 */
public class Instance02 {
    public int id = 1;
    private static Instance02 instance = new Instance02();

    public Instance02 getInstance() {
        return instance;
    }

    public static void main(String[] args) {
        Instance02 instance01 = new Instance02();
        Instance02 instance = instance01.getInstance();
        System.out.println(instance.id);
    }
}
