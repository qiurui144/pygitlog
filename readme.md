# pygitlog-tools
<table><tr>
<font face="黑体" size=4>git工具用于进行kernel相关的git log 可视化查看</font>

<font face="黑体" size=4>目标：建立跟踪与关联知识库的建立，进行人力评估统计，对patch进行有效分类</font>

<font face="黑体" size=4>主要适配社区：Kernel社区、Euler社区 </font>
</tr></table>  

# 示例
---

### kernel log summary
### upstream from 2c85ebc57b3e to 33dc9614dc20
|  hash  |  time  |  editor |  email |  body | type  |  keywords |  diff-files  | 
|  :---- | :----  |  :----  |  :---- |  :--- | :---- |  :------- |  :---------  | 
| 2c85ebc57b3e | Sun Dec 13 14:41:30 2020 -0800 | Linus Torvalds | torvalds@linux-foundation.org | <details><summary>Linux 5.10</summary> Linux 5.10<br></details> | <br> | [special](https://en.wikipedia.org/wiki/Special)<br> | Makefile |
| ec6f5e0e5ca0 | Sun Dec 13 11:31:19 2020 -0800 | Linus Torvalds | torvalds@linux-foundation.org | <details><summary>Merge tag 'x86-urgent-2020-12-13' of git://git.kernel.org/pub/scm/linux/kernel/git/tip/tip</summary> </details> | <br> | [special](https://en.wikipedia.org/wiki/Special)<br> | <details><summary>arch/x86/include/asm/pgtable_types.h</summary> arch/x86/include/asm/sync_core.h<br>arch/x86/kernel/apic/vector.c<br>arch/x86/kernel/cpu/resctrl/monitor.c<br>arch/x86/kernel/kprobes/opt.c<br>arch/x86/mm/mem_encrypt_identity.c<br>arch/x86/mm/tlb.c<br>kernel/sched/membarrier.c<br><br></details> |
| d2360a398f0b | Sun Dec 13 10:36:23 2020 -0800 | Linus Torvalds | torvalds@linux-foundation.org | <details><summary>Merge tag 'block-5.10-2020-12-12' of git://git.kernel.dk/linux-block</summary> Merge tag 'block-5.10-2020-12-12' of git://git.kernel.dk/linux-block<br><br>Pull block fixes from Jens Axboe:<br> "This should be it for 5.10.<br><br>  Mike and Song looked into the warning case, and thankfully it appears<br>  the fix was pretty trivial - we can just change the md device chunk<br>  type to unsigned int to get rid of it. They cannot currently be < 0,<br>  and nobody is checking for that either.<br><br>  We're reverting the discard changes as the corruption reports came in<br>  very late, and there's just no time to attempt to deal with it at this<br>  point. Reverting the changes in question is the right call for 5.10"<br><br>* tag 'block-5.10-2020-12-12' of git://git.kernel.dk/linux-block:<br>  md: change mddev 'chunk_sectors' from int to unsigned<br>  Revert "md: add md_submit_discard_bio() for submitting discard bio"<br>  Revert "md/raid10: extend r10bio devs to raid disks"<br>  Revert "md/raid10: pull codes that wait for blocked dev into one function"<br>  Revert "md/raid10: improve raid10 discard request"<br>  Revert "md/raid10: improve discard request for far layout"<br>  Revert "dm raid: remove unnecessary discard limits for raid10"<br></details> | <br> | [mdadm](https://en.wikipedia.org/wiki/Mdadm)<br> | <details><summary>drivers/md/dm-raid.c</summary> drivers/md/md.c<br>drivers/md/md.h<br>drivers/md/raid0.c<br>drivers/md/raid10.c<br>drivers/md/raid10.h<br><br></details> |
| 6bff9bb8a292 | Sat Dec 12 12:57:12 2020 -0800 | Linus Torvalds | torvalds@linux-foundation.org | <details><summary>Merge tag 'scsi-fixes' of git://git.kernel.org/pub/scm/linux/kernel/git/jejb/scsi</summary> Merge tag 'scsi-fixes' of git://git.kernel.org/pub/scm/linux/kernel/git/jejb/scsi<br><br>Pull SCSI fixes from James Bottomley:<br> "Five small fixes.  Four in drivers:<br><br>   - hisi_sas: fix internal queue timeout<br><br>   - be2iscsi: revert a prior fix causing problems<br><br>   - bnx2i: add missing dependency<br><br>   - storvsc: late arriving revert of a problem fix<br><br>  and one in the core.<br><br>  The core one is a minor change to stop paying attention to the busy<br>  count when returning out of resources because there's a race window<br>  where the queue might not restart due to missing returning I/O"<br><br>* tag 'scsi-fixes' of git://git.kernel.org/pub/scm/linux/kernel/git/jejb/scsi:<br>  Revert "scsi: storvsc: Validate length of incoming packet in storvsc_on_channel_callback()"<br>  scsi: hisi_sas: Select a suitable queue for internal I/Os<br>  scsi: core: Fix race between handling STS_RESOURCE and completion<br>  scsi: be2iscsi: Revert "Fix a theoretical leak in beiscsi_create_eqs()"<br>  scsi: bnx2i: Requires MMU<br></details> | <br> | [scsi](https://en.wikipedia.org/wiki/SCSI)<br> | <details><summary>drivers/scsi/be2iscsi/be_main.c</summary> drivers/scsi/bnx2i/Kconfig<br>drivers/scsi/hisi_sas/hisi_sas_main.c<br>drivers/scsi/hisi_sas/hisi_sas_v3_hw.c<br>drivers/scsi/scsi_lib.c<br>drivers/scsi/storvsc_drv.c<br><br></details> |
| 5ee595d9079b | Sat Dec 12 12:47:46 2020 -0800 | Linus Torvalds | torvalds@linux-foundation.org | <details><summary>Merge branch 'i2c/for-current' of git://git.kernel.org/pub/scm/linux/kernel/git/wsa/linux</summary> Merge branch 'i2c/for-current' of git://git.kernel.org/pub/scm/linux/kernel/git/wsa/linux<br><br>Pull i2c fix from Wolfram Sang:<br> "Bugfix for the AT24 EEPROM driver"<br><br>* 'i2c/for-current' of git://git.kernel.org/pub/scm/linux/kernel/git/wsa/linux:<br>  misc: eeprom: at24: fix NVMEM name with custom AT24 device name<br></details> | <br> | [special](https://en.wikipedia.org/wiki/Special)<br> | drivers/misc/eeprom/at24.c |

***
---
# 学习链接
<font face="黑体" size=4>[How to create a Python library](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f)  </font>

<font face="黑体" size=4>[Wiki API](https://www.mediawiki.org/wiki/API:Search)  </font>

<font face="黑体" size=4>[Git book](https://git-scm.com/docs/)  </font>