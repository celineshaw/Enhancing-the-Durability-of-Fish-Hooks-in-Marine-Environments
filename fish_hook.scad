
    // Function to create a rotated hook shape
    module rotated_hook() {
        rotate_extrude($fn=100)
        translate([hook_radius, 0])
        circle(d=hook_thickness);
    }
    
    // Function to create the hook shank
    module hook_shank() {
        cylinder(h=shank_length, r1=hook_thickness/2, r2=hook_thickness/2, $fn=100);
    }
    
    // Function to create the barb
    module barb() {
        linear_extrude(height=barb_width, center=true, convexity=10)
        polygon(points=[[0,0],[barb_length*cos(45),-barb_length*sin(45)],[0,-2*barb_length*sin(45)]]);
    }
    
    // Assembling the hook
    difference() {
        union() {
            rotated_hook();
            translate([0, 0, -hook_thickness/2])
            hook_shank();
        }
        translate([0, hook_radius - barb_length, -hook_thickness])
        rotate([0, 0, 180])
        barb();
    }
    
    // Render the fish hook
    rotated_hook();
    