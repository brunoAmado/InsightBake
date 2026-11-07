// SetMiddle Insight™ · Bake — Rust Structural & Dowel Load Verifier (`:4030`)
pub fn verify_tier_stability(bottom_diameter_cm: f64, top_diameter_cm: f64, total_height_cm: f64) -> bool {
    top_diameter_cm <= bottom_diameter_cm && (total_height_cm / bottom_diameter_cm.max(1.0)) <= 2.2
}

fn main() {
    println!("SetMiddle Insight™ · Bake Rust Structural Engine Ready (:4030)");
}
