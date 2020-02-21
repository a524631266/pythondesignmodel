package build.singledesign.enumdemo;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

public class Demo {
    private AtomicInteger id = new AtomicInteger(0);
    private Demo(){}
    enum  InstanceEnum{
        INSTANCE;
        private final Demo instance;
        InstanceEnum(){
            instance = new Demo();
        }

        public Demo getInstance(){
            return instance;
        }
    }

    public static Demo getInstance(){
        return InstanceEnum.INSTANCE.getInstance();
    }

    public int getId() {
        return id.getAndIncrement();
    }

    public static void main(String[] args) {
        IntStream.rangeClosed(0,10).forEach(i -> {
            new Thread(()->{
                System.out.println(Demo.getInstance().getId());
            }).start();
        });
    }

}
