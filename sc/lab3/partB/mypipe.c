#include <linux/init.h>
#include <linux/module.h>
#include <linux/types.h>
#include <linux/fs.h>
#include <linux/cdev.h>

#include "buff_helper.h"

MODULE_LICENSE("Dual BSD/GPL");
MODULE_AUTHOR("SC2022/2023");
MODULE_DESCRIPTION("Simple pipe character device driver");
MODULE_VERSION("0:0.1");

/** module functions **/
static int mypipe_init(void);
static void mypipe_exit(void);

/** device driver functions  **/
static int mypipe_open(struct inode *inode, struct file *filp);
static int mypipe_release(struct inode *inode, struct file *filp);
ssize_t mypipe_read(struct file *filep, char __user *buff, size_t count, loff_t *offp);
ssize_t mypipe_write(struct file *filep, const char __user *buff, size_t count, loff_t *offp);

/**  global variables for the device driver  **/
static dev_t mydev;
static struct cdev *mycdev;
static struct file_operations myfops = {
    .owner = THIS_MODULE,
	.read = mypipe_read,
	.write = mypipe_write,
	.open = mypipe_open,
	.release = mypipe_release
};
/***********/
#define BUFFER_MAX_SIZE 100

char data_space[BUFFER_MAX_SIZE];
circ_buff_t mypipe_buffer = { 
    data_space,
    BUFFER_MAX_SIZE,
    0,
    0
};
/************/
static int mypipe_open(struct inode *inode, struct file *filp)
{
	// Debug:
	printk(KERN_INFO "mypipe_open(): Returning\n");
    return -1;
}
/************/
static int mypipe_release(struct inode *inode, struct file *filp)
{
	// Debug:
    printk(KERN_INFO "mypipe_release(): Returning\n");
    return 1;
}
/************/
ssize_t mypipe_read(struct file *filep, char __user *buff, size_t count, loff_t *offp)
{
    // Should read data from circ_buffer and transfer it to user space.

	// Debug:
	printk(KERN_INFO "mypipe_read(): Read X characters\n");
	return 0;
}
/************/
ssize_t mypipe_write(struct file *filep, const char __user *buff, size_t count, loff_t *offp)
{
    // Should write data from user space to circ_buffer.

	// DON'T FORGET TO NEVER RETURN A CONSTANT ZERO VALUE

	// Debug:
	printk(KERN_INFO "mypipe_write(): Wrote X characters\n");
	return -1;
}
/**************/
static int mypipe_init(void)
{
	int result = -1;

	// Register device driver so that:
	// - Driver name is mypipe 
	// - Major number is dynamically assigned
	// - Minor number starts from 0
	// - Only one device needs to be managed by the driver

	if (result < 0){
		printk(KERN_ERR "Failed to register mypipe device driver\n");
		return result;
	}

    // Create struture to represent char devices

    // Register character device into the kernel

    if (result < 0){
        printk(KERN_ERR "Failed to register character device info\n");
        return result;
    }

	// Print "mypipe device driver registered with major number X"
	// to the kernel logging buffer so that:
	// - X is the obtained major number during registration
	// - Message printed using the informational log evel
	printk(KERN_INFO "mypipe device driver registered with major number X\n");
	return 0;
}
/************/
static void mypipe_exit(void)
{
    // deregister character device

    // deregister the device driver's device numbers

	// print "mypipe device driver deregistered" to the kernel
	// logginf buffer using the information log level
	printk(KERN_INFO "mypipe device driver deregistered\n");
}
/************/
module_init(mypipe_init);
module_exit(mypipe_exit);