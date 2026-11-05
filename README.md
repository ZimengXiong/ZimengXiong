I really really like 3D printing<sub>1</sub>, anything electronic<sub>2</sub>, self-hosting<sub>3</sub>, and, depending on the month, a type of robotics<sub>4</sub>. I also work very hard to maintain my 6-hour P99 SLA on e-mail :)

<sub>**1.** Until it is "solved," my biggest dream is to help bring in a non-planar revolution (we can't let slicers stagnate!!)</sub><br>
<sub>**2.** That is, microcontrollers, inverse kinematics, motion controllers, hardware hacking, machine learning (sorry for the buzzword), FPGA & ASIC design, algorithms, and probably a lot of things I'm forgetting. I also really enjoy working out and whiteboarding state machines</sub><br>
<sub>**3.** I particularly enjoy satisfying web design and the thrill of opening a link to *.alpacawebservices.com, where most of my self hosted services live</sub><br>
<sub>**4.** Currently, that is FOC & training robots with MuJoCo</sub>

## my favorite things that I {have, am, want} {worked, working, to work} on

<details>
<summary>Dual robot arm non-planar 3D printing</summary>

it turns out [these arms](https://www.seeedstudio.com/reBot-Arm-B601-RS-Assembled-Kit-with-Gripper-p-6865.html) are pretty bad for tracking accuracy. so i am looking into switching to this [unitree arm](https://shop.unitree.com/products/unitree-bionic-7-axis-dexterous-robotic-arm?variant=51885386760425) (also cheaper!)

<p>
  <a href="images/dual-arm-printer-collage.webp"><img src="images/dual-arm-printer-collage.webp" width="90%" alt="Dual robot arm printing setup above two views of the non-planar benchmark"></a>
</p>

(bottom: a benchy-derived test object I designed for measuring non-planar capabilities)

</details>

<details>
<summary>Robots!!</summary>

<p>
  <a href="videos/robot-arm-demo.mp4"><img src="images/robot-arm-demo-preview.webp" width="36%" align="top" alt="Robot arm demo; click for the full video"></a> <a href="videos/quadruped-robot-demo.mp4"><img src="images/quadruped-robot-demo-preview.webp" width="36%" align="top" alt="Quadruped robot demo; click for the full video"></a>
</p>

</details>

<details>
<summary>PancakeSlicer: self-hostable non-planar slicing for 3-axis, 5-axis, 6/7 (haha) DOF robot arms. <a href="https://pancake.cooking/">[link]</a></summary>
some cool highlights

1. slice from any browser (phone, ipad, anything)
2. no need for tunneling services (bambu connect, etc) since it's self hosted and everything routes through your server
3. no need for syncing profiles between devices since its all server side
4. has the best profile management solution of any slicer in existence (IMO). iykyk no more having fifty slightly different `0.20mm STANDARD @BBL A1 mini 0.4mm` and whatnot. we use dynamic profiles -> auto-configure based on layer height and printer settings, so we only store the actual things you want in a profile (infill type, support, perimeter counts). this means you can use a profile, for the first time, *across* printers.
5. because it's built on web standards, things behave normally instead of on the (legendary, but really it's time to retire from) `wxWidgets` GUI framework. you know how copy pasting and even things like text selection don't work consistently? and how menus lag to open? yeah, that's all fixed now it's all the oh so beautiful web. i ❤️ web standards. and yes don't come at me it's built with electron (go look at webkit (safari) graphics performance and then come tell me you wouldn't do the same)

<p>
  <a href="images/pancakeslicer-desktop.webp"><img src="images/pancakeslicer-desktop.webp" width="78%" align="top" alt="PancakeSlicer desktop comparison of planar and non-planar slicing"></a> <a href="images/pancakeslicer-mobile.webp"><img src="images/pancakeslicer-mobile.webp" width="20%" align="top" alt="PancakeSlicer running on a phone"></a>
</p>

(in the left screenshot: planar slicing on the left, non planar on the right, you can see the difference in mean surface error)

(in the right screenshot you should be amazed that this is even possible!!)

</details>

<details>
<summary>WinMux: the bestest window manager ever <a href="https://winmux.dev/">[link]</a></summary>
self explanatory, but

1. we have sidebars
2. we have ["window tabs"](https://www.winmux.dev/tab-groups.mp4) where you can stack multiple windows on top of each other and tab between them as if they are browser tabs
3. we have [double sided windows](https://www.reddit.com/r/MacOS/comments/1wed10s/double_sided_windows_in_winmux_054/) (yes, literally)
4. we have sidebars

![](images/winmux-desktop.webp)

</details>

<details>
<summary>A story in three acts</summary>

<p>
  <a href="images/macbook-storage-1tb.webp"><img src="images/macbook-storage-1tb.webp" width="49%" alt="Macintosh HD with 1 TB of storage"></a><br>
  <a href="videos/macbook-storage-chip-replacement.mp4"><img src="images/macbook-storage-chip-replacement-preview.webp" width="49%" alt="Storage chip replacement video; click for the full video"></a><br>
  <a href="images/macbook-storage-8tb.webp"><img src="images/macbook-storage-8tb.webp" width="49%" alt="Macintosh HD with 8 TB of storage"></a>
</p>

</details>

<details>
<summary>Printers &amp (one) <a href="https://github.com/ZimengXiong/ScrapNC/">CNC</a> I have designed/assembeled and built over the years</summary>
<p>
  <a href="images/printers-and-cnc-collage.webp"><img src="images/printers-and-cnc-collage.webp" width="100%" alt="Seventeen photos of CNC builds, printers, electronics, and motion platforms arranged in five rows"></a>
</p>

</details>

<details>
<summary>some art</summary>

<p>
  <a href="images/art-collage.webp"><img src="images/art-collage.webp" width="100%" alt="Eight art pieces arranged in a collage"></a>
</p>

</details>
