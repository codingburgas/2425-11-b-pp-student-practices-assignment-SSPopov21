import React, { useState } from "react";
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
import { cn } from "@/lib/utils";

type JobApplication = {
  id: number;
  company: string;
  position: string;
  date: string;
  status: 'applied' | 'interview' | 'offer' | 'rejected';
  priority: 'low' | 'medium' | 'high';
  notes?: string;
  skills: string[];
  creator: string;
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
      skills: ["React", "TypeScript", "Tailwind CSS"],
      creator: "John Doe"
    },
    {
      id: 2,
      company: "DataSystems",
      position: "Machine Learning Engineer",
      date: "2025-05-15",
      status: "applied",
      priority: "medium",
      skills: ["Python", "TensorFlow", "Data Science"],
      creator: "Jane Smith"
    },
    {
      id: 3,
      company: "WebScale",
      position: "Full Stack Developer",
      date: "2025-05-10",
      status: "offer",
      priority: "high",
      notes: "Received offer, negotiating salary",
      skills: ["Node.js", "React", "MongoDB"],
      creator: "Mike Johnson"
    },
    {
      id: 4,
      company: "CloudNative",
      position: "DevOps Engineer",
      date: "2025-05-05",
      status: "rejected",
      priority: "low",
      notes: "Position filled internally",
      skills: ["Docker", "Kubernetes", "AWS"],
      creator: "Sarah Wilson"
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

  const getStatusClass = (status: JobApplication['status']) => {
    switch (status) {
      case 'applied': return 'bg-blue-500 hover:bg-blue-600';
      case 'interview': return 'bg-yellow-500 hover:bg-yellow-600';
      case 'offer': return 'bg-green-500 hover:bg-green-600';
      case 'rejected': return 'bg-red-500 hover:bg-red-600';
      default: return 'bg-gray-500 hover:bg-gray-600';
    }
  };

  const getPriorityClass = (priority: JobApplication['priority']) => {
    switch (priority) {
      case 'high': return 'bg-red-500 hover:bg-red-600';
      case 'medium': return 'bg-yellow-500 hover:bg-yellow-600';
      case 'low': return 'bg-green-500 hover:bg-green-600';
      default: return 'bg-gray-500 hover:bg-gray-600';
    }
  };

  const handleDelete = (id: number) => {
    setApplications(applications.filter(app => app.id !== id));
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
                <TableHead 
                  onClick={() => requestSort('creator')}
                  className="cursor-pointer hover:bg-gray-50"
                >
                  Created By
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
                    <span className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold ${getStatusClass(application.status)}`}>
                      {application.status.charAt(0).toUpperCase() + application.status.slice(1)}
                    </span>
                  </TableCell>
                  <TableCell>
                    <span className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold ${getPriorityClass(application.priority)}`}>
                      {application.priority.charAt(0).toUpperCase() + application.priority.slice(1)}
                    </span>
                  </TableCell>
                  <TableCell>{application.creator}</TableCell>
                  <TableCell className="space-x-2">
                    <Button variant="outline" size="sm">Edit</Button>
                    <Button 
                      variant="destructive" 
                      size="sm"
                      onClick={() => handleDelete(application.id)}
                    >
                      Delete
                    </Button>
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
