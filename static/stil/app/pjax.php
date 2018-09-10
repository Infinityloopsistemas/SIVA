<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- PJAX
                    ====================== -->
                    <div class="callout callout-info">
                        <h4>Get Started</h4>
                        <p>Stilearn Admin 2.x was developed with the support PJAX (if you do not want to use it you can remove it). If you are not familiar pjax, please go to the <a target="_blank" href="https://github.com/defunkt/jquery-pjax">Project Page</a> to read the documentation.</p>
                    </div>

                    <div class="page-header">
                        <h3>How to activate PJAX on this theme?</h3>
                    </div>

                    <p>You can activate pjax with element <code>&lt;a&gt;</code> whenever you want. Just need to add the attribute <code>data-pjax="target-container"</code> (Or try to define with Your own selector). <code>target-container</code> is the place where the target pjax will be loaded.</p>
                    <p>We also added support for <code>animation.css</code> on pjax page. Animation will be added to the <code>target-container</code> automatically after pjax (default is <code>fadeInDown</code>). You can use the animation that you like by adding the <code>data-animatedpjax="animateInValue"</code>. Refer to demo below to see this in action.</p>
                    <p><a href="pjax.php" data-pjax=".content-body" data-animatedpjax="slideInDown">Pjax with custom Animated</a> Or try other Animated:</p>
                    <div class="row">
                        <div class="col-md-4">
                            <div class="list-group">
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="bounce">bounce</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="flash">flash</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="pulse">pulse</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="shake">shake</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="swing">swing</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="tada">tada</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="wobble">wobble</a>
                            </div>
                        </div>

                        <div class="col-md-4">
                            <div class="list-group">
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="bounceIn">bounceIn</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="bounceInUp">bounceInUp</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="flipInX">flipInX</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="flipInY">flipInY</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="rotateIn">rotateIn</a>
                                <a class="list-group-item" href="pjax.php" data-pjax=".content-body" data-animatedpjax="rollIn">rollIn</a>
                                <a class="list-group-item" target="_blank" href="http://daneden.github.io/animate.css/">and more...</a>
                            </div>
                        </div>
                    </div>

                    <div class="callout callout-warning">
                        <h4>Script Execution</h4>
                        <p>PJAX (after pjax complete) automatically Reload <code>&lt;script&gt;</code> that has a class <code>.re-execute</code> and remove old Re-execute Script(s). So You must manage your re-execute script(s) (if any) for custom usage.</p>
                        <p>Just add <code>.re-execute</code> to <code>&lt;script&gt;</code>, so PJAX read your <code>script</code> as a Re-execute Script. <strong>Very Easy!</strong></p>
                    </div>