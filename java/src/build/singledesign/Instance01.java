package build.singledesign;

/**
 * 错误的方法,如果只是使用一个内部成员变量,调用自身会出现迭代死循环
 */
public class Instance01 {
    public int id = 1;
    private Instance01 instance = new Instance01();

    public Instance01 getInstance() {
        return instance;
    }

    public static void main(String[] args) {
        Instance01 instance01 = new Instance01();
        Instance01 instance = instance01.getInstance();
        System.out.println(instance.id);
    }
}
