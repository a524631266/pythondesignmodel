package build.singledesign;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * 实际案例  饿汉式
 * 1. 构造器需要私有,防止被new
 * 2. 考虑对象实现的线程安全问题
 * 3.考虑是否支持延迟(懒加载)
 * 4.getInstance是否高效
 */
public class IdGeneratorDemo {
    static class IdGenerator{
        private AtomicInteger id = new AtomicInteger(0);
        private static IdGenerator idGenerator = new IdGenerator();
        private IdGenerator(){}

        public static IdGenerator getInstance() {
            return idGenerator;
        }

        public int getId() {
            return id.getAndIncrement();
        }
    }
    public static void main(String[] args) {
        for (int i = 0; i < 100; i++) {
            new Thread(()->{
                System.out.println(IdGenerator.getInstance().getId());

            }).start();
        }
    }
}
