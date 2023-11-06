### 你好👋，我是许聚展

- 🔭 I’m currently a Ph.D. student in Computer Science supervised by Prof. Ruizhen Hu, working in Visual Computing Research Center, Shenzhen University.
- 🌱 I am interested in Computer Graphics, Robotics and Reinforcement Learning.
- 🪵 I am also interested in blender.

<style>
    .pub {
        text-align: center;
        margin: 0 auto;
        width: 98%;
        min-width: 600px;
        height: 150px;
        border: 1px solid #555;
        border-radius: 5px;
        position: relative;
        
        overflow: hidden;
        text-overflow:ellipsis;
        white-space: normal;

        margin-top: 10px;
        padding: 10px;

        
    }
    .pub > div {
        padding: 10px;

        position: absolute;
        top: 0;
        bottom: 0;

    }
    .pub_img {        
        margin: auto;
    }
    .pub_img_div {
        display: flex;
        width: 24%;
        left: 0;
        
    }
    .pub_info_div {

        text-align: left;
        width: 70%;
        padding: 0px 15px;

        right: 0;
    }

    .pub_title {
        font-weight: bold;
    }
    .pub_org {
        color: #aaa;
    }
    
</style>

<h3>Research</h3>

<!-- ######################################################## -->

<div class='pub'>

<div class="pub_img_div">
    <img class='pub_img' src="./assets/tapnet++/img.jpg" alt="图片" >
</div>

<div class="pub_info_div">
<div class='pub_title'>Neural Packing: from Visual Sensing to Reinforcement Learning</div>
<div class='pub_person'>
Juzhan Xu, 
<a href="http://socs.uoguelph.ca/~minglun/">Minglun Gong</a>, 
<a href="http://www.cs.sfu.ca/~haoz/">Hao Zhang</a>, 
<a href="http://vcc.szu.edu.cn/~huihuang/">Hui Huang</a> and 
<a href="https://csse.szu.edu.cn/staff/ruizhenhu/index.htm">Ruizhen Hu</a>
</div>
<div class='pub_org'>
<em>ACM Transactions on Graphics</em>  (Proc. SIGGRAPH Asia), 42(6), 2023.
[<a href="https://vcc.tech/research/2023/TAPNet++">Project page</a>]
</div>
<br>
<p>A novel learning framework to solve the transport-and-packing (TAP) problem in 3D. It constitutes a full solution pipeline from partial observations of input objects via RGBD sensing and recognition to final box placement, via robotic motion planning, to arrive at a compact packing in a target container.</p>
<br>
</div>

</div>


<!-- ######################################################## -->
<div class='pub'>

<div class="pub_img_div">
    <img class='pub_img' src="./assets/nift/img.png" alt="图片" >
</div>

<div class="pub_info_div">
<div class='pub_title'>NIFT: Neural Interaction Field and Template for Object Manipulation</div>
<div class='pub_person'>
<a href="https://zzilch.github.io/">Zeyu Huang</a>, 
Juzhan Xu, 
<a href="#">Sisi Dai</a>, 
<a href="http://kevinkaixu.net/">Kai Xu</a>, 
<a href="http://www.cs.sfu.ca/~haoz/">Hao Zhang</a>, 
<a href="http://vcc.szu.edu.cn/~huihuang/">Hui Huang</a> and 
<a href="https://csse.szu.edu.cn/staff/ruizhenhu/index.htm">Ruizhen Hu</a>
</div>
<div class='pub_org'>
IEEE International Conference on Robotics and Automation (ICRA), 2023.
[<a href="https://vcc.tech/research/2023/NIFT">Project page</a>]
</div>
<br>
<p>We introduce NIFT, Neural Interaction Field and Template, a descriptive and robust interaction representation of object manipulations to facilitate imitation learning. Given a few object manipulation demos, NIFT guides the generation of the interaction imitation for a new object instance by matching the Neural Interaction Template (NIT) extracted from the demos to the Neural Interaction Field (NIF) defined for the new object.</p>
<br>
</div>

</div>


<!-- ######################################################## -->
<div class='pub'>

<div class="pub_img_div">
    <img class='pub_img' src="./assets/ibs_grasp/img.jpg" alt="图片" >
</div>

<div class="pub_info_div">
<div class='pub_title'>Learning High-DOF Reaching-and-Grasping via Dynamic Representation of Gripper-Object Interaction</div>
<div class='pub_person'>
<a href="#">Qijin She</a>, 
<a href="https://csse.szu.edu.cn/staff/ruizhenhu/index.htm">Ruizhen Hu</a>, 
Juzhan Xu, 
<a href="#">Min Liu</a>, 
<a href="http://kevinkaixu.net/">Kai Xu</a> and 
<a href="http://vcc.szu.edu.cn/~huihuang/">Hui Huang</a>
</div>
<div class='pub_org'>
ACM Transactions on Graphics (Proc. SIGGRAPH), 41(4): 97, 2022.
[<a href="https://vcc.tech/research/2022/Grasping">Project page</a>]
</div>
<br>
<p>We approach the problem of high-DOF reaching-and-grasping via learning joint planning of grasp and motion with deep reinforcement learning. To resolve the sample efficiency issue in learning the high-dimensional and complex control of dexterous grasping, we propose an effective representation of grasping state characterizing the spatial interaction between the gripper and the target object.</p>
<br>
</div>

</div>


<!-- ######################################################## -->
<div class='pub'>

<div class="pub_img_div">
    <img class='pub_img' src="./assets/upright/img.png" alt="图片" >
</div>

<div class="pub_info_div">
<div class='pub_title'>UprightRL: Upright Orientation Estimation of 3D Shapes via Reinforcement Learning</div>
<div class='pub_person'>
<a href="#">Luanmin Chen</a>, 
Juzhan Xu, 
<a href="#">Chuan Wang</a>, 
<a href="https://brotherhuang.github.io/">Haibin Huang</a>, 
<a href="http://vcc.szu.edu.cn/~huihuang/">Hui Huang</a> and 
<a href="https://csse.szu.edu.cn/staff/ruizhenhu/index.htm">Ruizhen Hu</a>
</div>
<div class='pub_org'>
Computer Graphics Forum (Proc. Pacific Graphics), 2021.
[<a href="https://vcc.tech/research/2021/UprightRL">Project page</a>]
</div>
<br>
<p>In this paper, we study the problem of 3D shape upright orientation estimation from the perspective of reinforcement learning, i.e. we teach a machine (agent) to orientate 3D shapes step by step to upright given its current observation. Unlike previous methods, we take this problem as a sequential decision-making process instead of a strong supervised learning problem. To achieve this, we propose UprightRL, a deep network architecture designed for upright orientation estimation.</p>
<br>
</div>

</div>

<!-- ######################################################## -->
<div class='pub'>

<div class="pub_img_div">
    <img class='pub_img' src="./assets/starglyph/img.png" alt="图片" >
</div>

<div class="pub_info_div">
<div class='pub_title'>Shape-driven Coordinate Ordering for Star Glyph Sets via Reinforcement Learning</div>
<div class='pub_person'>
<a href="https://csse.szu.edu.cn/staff/ruizhenhu/index.htm">Ruizhen Hu</a>, 
<a href="#">Bin Chen</a>, 
Juzhan Xu, 
<a href="http://people.scs.carleton.ca/~olivervankaick/index.html">Oliver van Kaick</a>, 
<a href="https://www.cgmi.uni-konstanz.de/">Oliver Deussen</a> and 
<a href="http://vcc.szu.edu.cn/~huihuang/">Hui Huang</a>
</div>
<div class='pub_org'>
IEEE Transactions on Visualization and Computer Graphics, 2021.
[<a href="https://vcc.tech/research/2021/STAR">Project page</a>]
</div>
<br>
<p>We present a neural optimization model trained with reinforcement learning to solve the coordinate ordering problem for sets of star glyphs. Given a set of star glyphs associated to multiple class labels, we propose to use shape context descriptors to measure the perceptual distance between pairs of glyphs, and use the derived silhouette coefficient to measure the perception of class separability within the entire set.</p>
<br>
</div>

</div>


<!-- ######################################################## -->
<div class='pub'>

<div class="pub_img_div">
    <img class='pub_img' src="./assets/tapnet/img.png" alt="图片" >
</div>

<div class="pub_info_div">
<div class='pub_title'>TAP-Net: Transport-and-Pack using Reinforcement Learning</div>
<div class='pub_person'>
<a href="https://csse.szu.edu.cn/staff/ruizhenhu/index.htm">Ruizhen Hu</a>, 
Juzhan Xu, 
<a href="#">Bin Chen</a>, 
<a href="http://socs.uoguelph.ca/~minglun/">Minglun Gong</a>, 
<a href="http://www.cs.sfu.ca/~haoz/">Hao Zhang</a> and 
<a href="http://vcc.szu.edu.cn/~huihuang/">Hui Huang</a>
</div>
<div class='pub_org'>
<em>ACM Transactions on Graphics</em>  (Proc. SIGGRAPH Asia), 42(6), 2020.
[<a href="https://vcc.tech/research/2020/TAP">Project page</a>]
</div>
<br>
<p>We introduce the transport-and-pack (TAP) problem, a frequently encountered instance of real-world packing, and develop a neural optimization solution based on reinforcement learning. Given an initial spatial configuration of boxes, we seek an efficient method to iteratively transport and pack the boxes compactly into a target container.</p>
<br>
</div>
</div>