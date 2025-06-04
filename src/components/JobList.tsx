
import { useState } from "react";
import { 
  Card, 
  CardContent, 
  CardHeader, 
  CardTitle 
} from "@/components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";

type JobApplication = {
  id: number;
  company: string;
  position: string;
  date: string;
  status: 'applied' | 'interview' | 'offer' | 'rejected';
  priority: 'low' | 'medium' | 'high';
  notes?: string;
  skills: string[];
};

const JobList = () => {
  const [sortConfig, setSortConfig] = useState<{
    key: keyof JobApplication;
    direction: 'ascending' | 'descending';
  } | null>(null);

  // Mock data - would come from a backend in a real app
  const [applications, setApplications] = useState<JobApplication[]>([
    {
      id: 1,
      company: "TechCorp",
      position: "Senior Frontend Developer",
      date: "2025-05-18",
      status: "interview",
      priority: "high",
      notes: "Second interview scheduled for next week",
      skills: ["React", "TypeScript", "Tailwind CSS"]
    },
    {
      id: 2,
      company: "DataSystems",
      position: "Machine Learning Engineer",
      date: "2025-05-15",
      status: "applied",
      priority: "medium",
      skills: ["Python", "TensorFlow", "Data Science"]
    },
    {
      id: 3,
      company: "WebScale",
      position: "Full Stack Developer",
      date: "2025-05-10",
      status: "offer",
      priority: "high",
      notes: "Received offer, negotiating salary",
      skills: ["Node.js", "React", "MongoDB"]
    },
    {
      id: 4,
      company: "CloudNative",
      position: "DevOps Engineer",
      date: "2025-05-05",
      status: "rejected",
      priority: "low",
      notes: "Position filled internally",
      skills: ["Docker", "Kubernetes", "AWS"]
    }
  ]);

  const requestSort = (key: keyof JobApplication) => {
    let direction: 'ascending' | 'descending' = 'ascending';
    if (sortConfig && sortConfig.key === key && sortConfig.direction === 'ascending') {
      direction = 'descending';
    }
    setSortConfig({ key, direction });
  };

  const getSortedApplications = () => {
    if (!sortConfig) return applications;
    
    return [...applications].sort((a, b) => {
      if (a[sortConfig.key] < b[sortConfig.key]) {
        return sortConfig.direction === 'ascending' ? -1 : 1;
      }
      if (a[sortConfig.key] > b[sortConfig.key]) {
        return sortConfig.direction === 'ascending' ? 1 : -1;
      }
      return 0;
    });
  };

  const getStatusColor = (status: JobApplication['status']) => {
    switch (status) {
      case 'applied': return 'bg-blue-100 text-blue-800';
      case 'interview': return 'bg-yellow-100 text-yellow-800';
      case 'offer': return 'bg-green-100 text-green-800';
      case 'rejected': return 'bg-red-100 text-red-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const getPriorityColor = (priority: JobApplication['priority']) => {
    switch (priority) {
      case 'high': return 'bg-red-100 text-red-800';
      case 'medium': return 'bg-yellow-100 text-yellow-800';
      case 'low': return 'bg-green-100 text-green-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <Card className="shadow-md">
      <CardHeader>
        <CardTitle className="text-xl text-primary">Recent Applications</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="overflow-x-auto">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead 
                  onClick={() => requestSort('company')}
                  className="cursor-pointer hover:bg-gray-50"
                >
                  Company
                </TableHead>
                <TableHead 
                  onClick={() => requestSort('position')}
                  className="cursor-pointer hover:bg-gray-50"
                >
                  Position
                </TableHead>
                <TableHead 
                  onClick={() => requestSort('date')}
                  className="cursor-pointer hover:bg-gray-50"
                >
                  Date Applied
                </TableHead>
                <TableHead 
                  onClick={() => requestSort('status')}
                  className="cursor-pointer hover:bg-gray-50"
                >
                  Status
                </TableHead>
                <TableHead 
                  onClick={() => requestSort('priority')}
                  className="cursor-pointer hover:bg-gray-50"
                >
                  Priority
                </TableHead>
                <TableHead>Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {getSortedApplications().map((application) => (
                <TableRow key={application.id} className="hover:bg-gray-50">
                  <TableCell className="font-medium">{application.company}</TableCell>
                  <TableCell>{application.position}</TableCell>
                  <TableCell>{new Date(application.date).toLocaleDateString()}</TableCell>
                  <TableCell>
                    <Badge className={getStatusColor(application.status)}>
                      {application.status.charAt(0).toUpperCase() + application.status.slice(1)}
                    </Badge>
                  </TableCell>
                  <TableCell>
                    <Badge className={getPriorityColor(application.priority)}>
                      {application.priority.charAt(0).toUpperCase() + application.priority.slice(1)}
                    </Badge>
                  </TableCell>
                  <TableCell>
                    <Button variant="outline" size="sm">Edit</Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </CardContent>
    </Card>
  );
};

export default JobList;
