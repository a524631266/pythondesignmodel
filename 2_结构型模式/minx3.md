2.5. Overview of Processes in MINIX 3

Having completed our study of the principles of process management, interprocess communication, and scheduling, we can now take a look at how they are applied in MINIX 3. Unlike UNIX, whose kernel
is a monolithic program not split up into modules, MINIX 3 itself is a collection of processes that communicate with each other and also with user processes, using a single interprocess communication primitivemessage passing. This design gives a more modular
and flexible structure, making it easy, for example, to replace the entire file system by a completely different one, without having even to recompile the kernel
MINIX自身是一个进程的集合，这些进程不仅互相之间进行通信，也和用户进程进行通信，这种进程间的通信是一种灵活地消息传递。这样的设计给予了我们一个更加模块化和灵活的结构，比如说，我们可以替换整个文件系统而不需要重新编译内核。




The kernel in the bottom layer schedules processes and manages the transitions between the ready, running, and blocked states of Fig. 2-2. The kernel also handles all messages between processes. Message handling requires checking
for legal destinations, locating the send and receive buffers in physical memory, and copying bytes from sender to receiver. Also part of the kernel is support for access to I/O ports and interrupts, which on modern processors require use of privileged kernel
mode instructions not available to ordinary processes.

Minix3由四个不同的层次组成，最底层的kernel用来调度进程以及管理进程之间的状态切换（运行，就绪，阻塞），kernel也对进程的所有消息进行操作，这些操作包括检查消息的目的地是否合法，定位在内存中的发送和接收缓冲区，以及将字节从发送者复制到接受者。kernel的一些部分也支持对IO端口的访问和中断处理，这对于现代处理器来说是需要具有特权的内核态指令的，而这些指令对于普通的过程来说是不可能的。

In addition to the kernel itself, this layer contains two modules that function similarly to device drivers. Theclock task is an I/O device driver in the sense that it interacts with the hardware that generates timing signals, but
it is not user-accessible like a disk or communications line driverit interfaces only with the kernel.
One of the main functions of layer 1 is to provide a set of privileged kernel calls to the drivers and servers above it. These include reading and writing I/O ports, copying data between address spaces, and so on. Implementation of these calls is done by the
system task. Although the system task and the clock task are compiled into the kernel's address space, they are scheduled as separate processes and have their own call stacks.

除了kernel，底层还包括另外两个模块，他们的功能和设备驱动器相似。clock task模块是一个I/O设备驱动，这意味着它和硬件进行交互产生时间信号，但是这个模块是用户无法访问的

底层主要的功能是为上层的驱动器和服务器提供一组内核调用(kernel calls),包括读写I/O端口，在地址空间之间复制数据等等，这些调用是由system task模块实现的。虽然system task和clock task被编译进内核地址空间，但他们被作为两个不同的进程进行调度，而且拥有自己的调用栈。


Most of the kernel and all of the clock and system tasks are written in C. However, a small amount of the kernel is written in assembly language. The assembly language parts deal with interrupt handling, the low-level mechanics
of managing context switches between processes (saving and restoring registers and the like), and low-level parts of manipulating the MMU hardware. By and large, the assembly-language code handles those parts of the kernel that deal directly with the hardware
at a very low level and which cannot be expressed in C. These parts have to be rewritten when MINIX 3 is ported to a new architecture.
The three layers above the kernel could be considered to be a single layer because the kernel fundamentally treats them all of them the same way. Each one is limited to user mode instructions, and each is scheduled to run by the kernel. None of them can access
I/O ports directly. Furthermore, none of them can access memory outside the segments allotted to it.
However, processes potentially have special privileges (such as the ability to make kernel calls). This is the real difference between processes in layers 2, 3, and 4. The processes in layer 2 have the most privileges, those in layer 3 have some privileges,
and those in layer 4 have no special privileges. For example, processes in layer 2, called device drivers, are allowed to request that the system task read data from or write data to I/O ports on their behalf. A driver is needed for each device type, including
disks, printers, terminals, and network interfaces. If other I/O devices are present, a driver is needed for each one of those, as well. Device drivers may also make other kernel calls, such as requesting that newly-read data be copied to the address space
of a different process.

这三个模块大部分是用C语言编写的，然后有很小一部分是用汇编语言编写的，用汇编语言的这小部分实现了中断处理，进程上下切换的底层部分和操纵MMU硬件的底层部分。

总的来说，汇编语言实现了kernel模块里那些直接面向硬件的部分。

kernel上面的三层可以被认为是三个独立的层次，因为kernel在根本上将他们以相同的方式对待。每一个部分都只能使用用户态的指令，且被kernel调度，没有任何一个可以直接访问I/O端口。此外，他们都不能访问那些并不是分配给他们的内存。

但是，进程潜在的拥有一些特别的权限（例如进行kernel calls),在第2，3，4层的进程拥有的这些权限都是不同的。第二层(device drivers)被允许请求system task对I/O端口进行读写数据，第二层也能进行kernel calls,例如请求将新数据复制到其他进程的地址空间。





The third layer contains servers, processes that provide useful services to the user processes. Two servers are essential. The process manager (PM) carries out all the MINIX 3 system calls that involve starting or stopping process
execution, such as fork, exec, and exit, as well as system calls related to signals, such as alarm and kill, which can alter the execution state of a process. The process manager also is responsible for managing memory, for instance, with the brk system call.
The file system (FS) carries out all the file system calls, such as read, mount, and chdir.
It is important to understand the difference between kernel calls and POSIX system calls. Kernel calls are low-level functions provided by the system task to allow the drivers and servers to do their work. Reading a hardware I/O port is a typical kernel call.
In contrast, the POSIX system calls such as read, fork, and unlink are high-level calls defined by the POSIX standard, and are available to user programs in layer 4. User programs contain many POSIX calls but no kernel calls. Occasionally when we are not being
careful with our language we may call a kernel call a system call. The mechanisms used to make these calls are similar, and kernel calls can be considered a special subset of system calls.
In addition to the PM and FS, other servers exist in layer 3. They perform functions that are specific to MINIX 3. It is safe to say that the functionality of the process manager and the file system will be found in any operating system. The information server
(IS) handles jobs such as providing debugging and status information about other drivers and servers, something that is more necessary in a system like MINIX 3, designed for experimentation, than would be the case for a commercial operating system which users
cannot alter. The reincarnation server (RS) starts, and if necessary restarts, device drivers that are not loaded into memory at the same time as the kernel. In particular, if a driver fails during operation, the reincarnation server detects this failure,
kills the driver if it is not already dead, and starts a fresh copy of the driver, making the system highly fault tolerant. This functionality is absent from most operating systems. On a networked system the optional network server (inet) is also in level
3. Servers cannot do I/O directly, but they can communicate with drivers to request I/O. Servers can also communicate with the kernel via the system task.

第三层包括一些服务器进程，这些进程为用户进程提供有用的服务。两个服务是必须的，process manager中实现了所有的MINIX3系统调用，包括fork,exec,exit,alarm,kill,brk。file system中实现了所有的文件调用，例如read mount chdir等等。

理解kernel call和POSIX system calls的区别很重要，kernal calls是由system task提供给驱动器和服务器的一些低级调用，例如读取I/O端口。相对的，POSIX system calls根据POSIX标准定义的高级调用，处在第四层的用户进程可以调用他们。

除了process manager和file system,其他的服务也都出现在第三层。information server处理一些作业，这些作业包括提供关于其他驱动器和服务器的调试和状态信息,这对于MINIX3很重要。此外reincarnation server也是一般操作系统没有的，networked system也在第三层。第三层的任何进程都不能直接I/O，但是他们可以和驱动器通信请求I/O。第三层也可以通过system task和kernel通信。





 In MINIX 3 the resource management is largely done by the drivers in layer 2, with help from the kernel layer when privileged access to I/O ports or the interrupt system is required. System call interpretation is done by the process
manager and file system servers in layer 3. The file system has been carefully designed as a file "server" and could be moved to a remote machine with few changes.

在MINIX 3中，资源管理很大一部交由第二层的驱动器，当需要特权访问I/O端口或者中断系统时寻求kernel层(底层)帮助。系统调用的是由第三层实现的，其中文件系统被仔细的设计成了一个文件服务器，这意味可以将它移动到一个远距离的机器上。





2.5.2. Process Management in MINIX 3

Processes in MINIX 3 follow the general process model described at length earlier in this chapter. Processes can create subprocesses, which in turn can create more subprocesses, yielding a tree of processes. In fact, all the user processes in the whole system
are part of a single tree with init (see Fig. 2-29) at the root. Servers and drivers are a special case, of course, since some of them must be started before any user process, including init.
曾个系统中所有的用户进程都是init的子进程。而servers和drivers层确实特殊的，他们在init进程启动前就已经开始运作了。

MINIX 3 Startup

When the computer is turned on, if the boot device is a diskette, the hardware reads the first sector of the first track of the boot disk into memory and executes the code it finds there. On a diskette this sector contains the bootstrap program. It is very
small, since it has to fit in one sector (512 bytes). The MINIX 3 bootstrap loads a larger program, boot, which then loads the operating system itself.

电脑启动的时候，如果启动盘是一个软盘，那么硬件会读取第一个扇区的内容到内存中，然周执行它们。在软盘中，这个扇区包括一个引导程序，它非常的小，一般不超过512bytes。MINIX 3引导程序载入一个大的程序boot,boot会载入操作系统。


In contrast, hard disks require an intermediate step. A hard disk is divided into partitions, and the first sector of a hard disk contains a small program and the disk's partition table. Collectively these two pieces are called the master boot record. The program
part is executed to read the partition table and to select the active partition. The active partition has a bootstrap on its first sector, which is then loaded and executed to find and start a copy of boot in the partition, exactly as is done when booting
from a diskette.

相对的，一个硬盘被分割为几个不同的分区，硬盘的第一个扇区包括一个小的程序和一个硬盘分区表。程序读取硬盘分区别然后选择一个主分区，在主分区的第一个扇区中存在引导程序。

In any case, the MINIX 3 boot program looks for a specific multipart file on the diskette or partition and loads the individual parts into memory at the proper locations. This is the boot image. The most important parts are the kernel (which include the clock
task and the system task), the process manager, and the file system. Additionally, at least one disk driver must be loaded as part of the boot image. There are several other programs loaded in the boot image. These include the reincarnation server, the RAM
disk, console, and log drivers, and init.

MINIX3 引导程序在软盘或者分区寻找特别的文件，然后加载进内存中的适当的地方。加载进内存的这些文件被称为引导镜像，最重要的一部分是kernel（包括clock task 和system task)，process manager,file system。此外，至少一个磁盘驱动器被加载作为引导镜像的一部分。reincarnation server ,RAM disk ,console ,log drivers 和init也被加载进来。

During its initialization phase the kernel starts the system and clock tasks, and then the process manager and the file system. The process manager and the file system then cooperate in starting other servers and drivers that are part of the boot image. When
all these have run and initialized themselves, they will block, waiting for something to do. MINIX 3 scheduling prioritizes processes. Only when all tasks, drivers, and servers loaded in the boot image have blocked will init, the first user process, be executed.
System components loaded with the boot image or during initialization are shown in Fig. 2-30。

process manager 和file system之后合作启动其他的servers 和drivers。当所有这些都运行并且初始化后，他们将被阻塞。当所有的tasks,drivers,servers都进入引导镜像并被阻塞后，第一个用户进程init将被运行。



Initialization of the Process Tree

Init is the first user process, and also the last process loaded as part of the boot image. You might think building of a process tree such as that of Fig. 1-5 begins once init starts running. Well, not exactly. That would be true in a conventional operating
system, but MINIX 3 is different. First, there are already quite a few system processes running by the time init gets to run. The tasks CLOCK and SYSTEM that run within the kernel are unique processes that are not visible outside of the kernel. They receive
no PIDs and are not considered part of any tree of processes. The process manager is the first process to run in user space; it is given PID 0 and is neither a child nor a parent of any other process. The reincarnation server is made the parent of all the
other processes started from the boot image (e.g., the drivers and servers). The logic of this is that the reincarnation server is the process that should be informed if any of these should need to be restarted.

init是第一个用户进程，也是最后一个被加载进引导镜像的进程。clock tasks ,system tasks是单独的进程，他们没有PID，所以不是进程树的一部分。process manager是第一个运行的用户空间中的进程，它被给予PID 0，不是任何进程的孩子或父进程。reincarnation server 是所有在引导镜像中开始运行的进程的父亲。逻辑上说这是因为如果由进程需要重新启动的话，他们都必须通知reincarnation server。

As we will see, even after init starts running there are differences between the way a process tree is built in MINIX 3 and the conventional concept. Init in a UNIX-like system is given PID 1, and even though init is not the first process to run, the traditional
PID 1 is reserved for it in MINIX 3. Like all the user space processes in the boot image (except the process manager), init is made one of the children of the reincarnation server. As in a standard UNIX-like system, init first executes the /etc/rc shell script.
This script starts additional drivers and servers that are not part of the boot image. Any program started by the rc script will be a child of init. One of the first programs run is a utility called service. Service itself runs as a child of init, as would
be expected. But now things once again vary from the conventional.