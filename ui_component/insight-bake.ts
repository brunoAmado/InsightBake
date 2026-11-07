// SetMiddle Insight™ · Bake — Three.js + ControlNet 3D Cake Configurator Web Component
export interface CakeTierSpec {
  shape: "ROUND" | "SQUARE" | "HEART" | "HEXAGON";
  diameter_cm: number;
  height_cm: number;
  sponge_id: string;
  filling_id: string;
  frosting_id: string;
  color_hex: string;
}
