
import 'lucide-react';

declare module 'lucide-react' {
  export const ChartLine: React.ForwardRefExoticComponent<
    Omit<React.SVGProps<SVGSVGElement>, "ref"> & {
      size?: string | number;
      strokeWidth?: string | number;
    } & React.RefAttributes<SVGSVGElement>
  >;
}
