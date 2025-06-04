
import React from "react";

export const ChartLine = React.forwardRef<SVGSVGElement, React.SVGProps<SVGSVGElement> & { size?: string | number; strokeWidth?: string | number }>(
  ({ color = "currentColor", size = 24, strokeWidth = 2, ...props }, ref) => (
    <svg
      ref={ref}
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke={color}
      strokeWidth={strokeWidth}
      strokeLinecap="round"
      strokeLinejoin="round"
      {...props}
    >
      <path d="M3 3v18h18" />
      <path d="m19 9-5 5-4-4-3 3" />
    </svg>
  )
);

ChartLine.displayName = "ChartLine";

export { Calendar, Briefcase, Plus, Settings, Check, Star, ArrowUp, ArrowDown, Mail, PlusCircle } from "lucide-react";
