<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- ANIMATED
                    ====================== -->
                    <div class="page-header">
                        <h3>Animate.css</h3>
                    </div>
                    <div class="callout callout-danger">
                        <p><code>Animate.css</code> is a bunch of cool, fun, and cross-browser animations for you to use in your projects. Great for emphasis, home pages, sliders, and general just-add-water-awesomeness. Please refer to <a rel="tooltip-right" data-html="true" title="Animate.css By <strong>Daneden</strong>" target="_blank" href="https://github.com/daneden/animate.css">Project Page</a> To used <code>animate.css</code>.</p>
                    </div>

                    <div class="page-header">
                        <h3>WOW.js</h3>
                    </div>

                    <div class="callout callout-warning">
                        <p>Reveal CSS animation as you scroll down a page. By default, you should use it to trigger <a rel="tooltip" data-html="true" title="Animate.css By <strong>Daneden</strong>" target="_blank" href="https://github.com/daneden/animate.css">animate.css</a> animations. But you can easily change the settings to your favorite animation library.</p>
                        <p>Please refer to <a rel="tooltip" data-html="true" title="WOW.js By <strong>Matthieu Aussaguel</strong>" target="_blank" href="https://github.com/matthieua/WOW">Project Page</a> To usage info.</p>
                    </div>

                    <div class="divider-content"><span></span></div>

                    <div class="page-header">
                        <h3>Hover.css</h3>
                    </div>

                    <p>A collection of CSS3 powered hover effects to be applied to call to actions, buttons, logos, featured images and so on. Easily apply to your own elements.</p>

                    <p class="text-muted"><strong>2D Transforms</strong></p>
                    <a class="hover-sample grow">Grow</a>
                    <a class="hover-sample shrink">Shrink</a>
                    <a class="hover-sample pulse-grow">Pulse Grow</a>
                    <a class="hover-sample pulse-shrink">Pulse Shrink</a>
                    <a class="hover-sample push">Push</a>
                    <a class="hover-sample pop">Pop</a>
                    <a class="hover-sample rotate">Rotate</a>
                    <a class="hover-sample grow-rotate">Grow Rotate</a>
                    <a class="hover-sample float">Float</a>
                    <a class="hover-sample sink">Sink</a>
                    <a class="hover-sample hover">Hover</a>
                    <a class="hover-sample hang">Hang</a>
                    <a class="hover-sample skew">Skew</a>
                    <a class="hover-sample skew-forward">Skew Forward</a>
                    <a class="hover-sample skew-backward">Skew Backward</a>
                    <a class="hover-sample wobble-horizontal">Wobble Horizontal</a>
                    <a class="hover-sample wobble-vertical">Wobble Vertical</a>
                    <a class="hover-sample wobble-to-bottom-right">Wobble To Bottom Right</a>
                    <a class="hover-sample wobble-to-top-right">Wobble To Top Right</a>
                    <a class="hover-sample wobble-top">Wobble Top</a>
                    <a class="hover-sample wobble-bottom">Wobble Bottom</a>
                    <a class="hover-sample wobble-skew">Wobble Skew</a>
                    <a class="hover-sample buzz">Buzz</a>
                    <a class="hover-sample buzz-out">Buzz Out</a>

                    <p class="text-muted margin-top"><strong>Border Transitions</strong></p>
                    <a class="hover-sample border-fade">Border Fade</a>
                    <a class="hover-sample hollow">Hollow</a>
                    <a class="hover-sample trim">Trim</a>
                    <a class="hover-sample outline-outward">Outline Outward</a>
                    <a class="hover-sample outline-inward">Outline Inward</a>
                    <a class="hover-sample round-corners">Round Corners</a>

                    <p class="text-muted margin-top"><strong>Shadow and Glow Transitions</strong></p>
                    <a class="hover-sample glow">Glow</a>
                    <a class="hover-sample box-shadow-outset">Box Shadow Outset</a>
                    <a class="hover-sample box-shadow-inset">Box Shadow Inset</a>
                    <a class="hover-sample float-shadow">Float Shadow</a>
                    <a class="hover-sample hover-shadow">Hover Shadow</a>
                    <a class="hover-sample shadow-radial">Shadow Radial</a>

                    <p class="text-muted margin-top"><strong>Speech Bubbles</strong></p>
                    <a class="hover-sample bubble-top">Bubble Top</a>
                    <a class="hover-sample bubble-right">Bubble Right</a>
                    <a class="hover-sample bubble-bottom">Bubble Bottom</a>
                    <a class="hover-sample bubble-left">Bubble Left</a>
                    <a class="hover-sample bubble-float-top">Bubble Float Top</a>
                    <a class="hover-sample bubble-float-right">Bubble Float Right</a>
                    <a class="hover-sample bubble-float-bottom">Bubble Float Bottom</a>
                    <a class="hover-sample bubble-float-left">Bubble Float Left</a>

                    <p class="text-muted margin-top"><strong>Curls</strong></p>
                    <a class="hover-sample curl-top-left">Curl Top Left</a>
                    <a class="hover-sample curl-top-right">Curl Top Right</a>
                    <a class="hover-sample curl-bottom-right">Curl Bottom Right</a>
                    <a class="hover-sample curl-bottom-left">Curl Bottom Left</a>

