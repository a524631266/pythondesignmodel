package build.singledesign;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

/**
 * 构造静态类方法
 */
public class StaticDemo {
    public AtomicInteger id = new AtomicInteger(0) ;
    // 在类加载过程只加载一次
    static {
        System.out.println("1111111111");
    }
    private StaticDemo(){}

    static class InnerStatic{
        public static StaticDemo instance = new StaticDemo();
    }

    public static StaticDemo getInstance(){
        return InnerStatic.instance;
    }

    public int getId() {
        return id.getAndIncrement();
    }

    public static void main(String[] args) {
//        int id = StaticDemo.id;
        IntStream.rangeClosed(0, 10).forEach(i->{
            new Thread(()->{
                System.out.println(StaticDemo.getInstance().getId());
            }).start();
        });
    }
}
