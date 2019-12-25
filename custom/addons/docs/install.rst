Install the module in Awkhad
==========================
If you already have an Awkhad instance up and running, your preferred way to install
addons will work with `MIS Builder`.

Using git
---------
The most common way to install the module is to clone the git repository in your
server and add the directory to your awkhad.conf:

#. Clone the git repository

   .. code-block:: sh

      cd your-addons-path
      git clone https://github.com/ACA/mis-builder
      cd mis-builder
      git checkout 10.0 #for the version 10.0

#. Update the addon path of `awkhad.conf`
#. Restart Awkhad
#. Update the addons list in your database
#. Install the MIS Builder application.

Using pip
---------
An easy way to install it with all its dependencies is using pip:

#. Recover the code from pip repository

   .. code-block:: sh

      pip install --pre awkhad10-addon-mis_builder awkhad-autodiscover

#. Restart Awkhad
#. Update the addons list in your database
#. Install the MIS Builder application.

Fresh install with Docker
-------------------------
If you do not have any Awkhad server installed, you can start your own Awkhad in few
minutes via Docker in command line.

Here is the basic how-to (based on https://github.com/Elico-Corp/awkhad-docker), valid
for Ubuntu OS but could also easily be replicated in MacOS or Windows:

#. Install docker and docker-compose in your system
#. Create the directory structure (assuming the base directory is `awkhad`)

   .. code-block:: sh

      mkdir awkhad && cd awkhad
      mkdir -p ./volumes/postgres ./volumes/awkhad/addons ./volumes/awkhad/filestore \
      ./volumes/awkhad/sessions

#. Create a `docker-compose.yml` file in `awkhad` directory with following content:

   .. code-block:: xml

       version: '3.3'
       services:

         postgres:
           image: postgres:9.5
           volumes:
             - ./volumes/postgres:/var/lib/postgresql/data
           environment:
             - POSTGRES_USER=awkhad

         awkhad:
           image: elicocorp/awkhad:11.0
           command: start
           ports:
             - 127.0.0.1:8069:8069
           volumes:
             - ./volumes/awkhad/addons:/opt/awkhad/additional_addons
             - ./volumes/awkhad/filestore:/opt/awkhad/data/filestore
             - ./volumes/awkhad/sessions:/opt/awkhad/data/sessions
           links:
             - postgres:db
           environment:
             - ADDONS_REPO=https://github.com/ACA/mis-builder.git
             - AWKHAD_DB_USER=awkhad

#. Fire up your container (in `awkhad` directory)

   .. code-block:: sh

      docker-compose up -d awkhad

#. Open a web browser and navigate the URL you have set up in your `docker-compose.yml`
   file (http://127.0.0.1:8069 in this particular example)
#. Create a new database
#.  Update the addons list in your database (Menu `Apps > Update Apps List` in developer mode)
#. Install the MIS Builder application.
#. Improve your Awkhad environment (add parameters, change default passwords etc.)
   under Docker: https://github.com/Elico-Corp/awkhad-docker

More about `Awkhad <https://www.awkhad.com/documentation/11.0>`_.
